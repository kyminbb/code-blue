from collections import defaultdict
from collections import deque
from typing import Dict
from typing import List
from typing import Tuple

import asyncio

from server.repositories.fcm_repository import FCMRepository
from server.repositories.db_repository import DBRepository
from server.schemas.emergency import DoctorMessage
from server.schemas.emergency import Emergency
from server.schemas.visitors import Doctor

# TODO: Initialize graph
graph = dict()


class EmergencyService:
    def __init__(self, db_repository: DBRepository, fcm_repository: FCMRepository):
        self.db_repository = db_repository
        self.fcm_repository = fcm_repository

    @classmethod
    async def _preprocess_doctors(cls, doctors: List[Doctor]) -> Dict[int, List[Tuple[str, str]]]:
        doctors_by_gates = defaultdict(list)
        for doctor in doctors:
            doctors_by_gates[doctor.gate].append((doctor.fcm_token, doctor.gate))
        return doctors_by_gates

    @classmethod
    async def _find_nearest_doctors(
        cls,
        patient_gate: int,
        doctors: Dict[int, List[Tuple[str, str]]],
        num_doctors: int = 3
    ) -> List[Tuple[str, str]]:
        # TODO: Convert to Dijkstra's to apply edge weights
        queue = deque([patient_gate])
        visited = {patient_gate}
        nearest_doctors = []
        while queue:
            gate = queue.popleft()
            gate_tokens = doctors[gate]
            nearest_doctors.extend(gate_tokens)
            if len(nearest_doctors) >= num_doctors:
                return nearest_doctors[:num_doctors]
            for neighbor_gate in graph[gate]:
                if neighbor_gate not in visited:
                    visited.add(neighbor_gate)
                    queue.append(neighbor_gate)
        return nearest_doctors

    async def handle_emergency(self, emergency: Emergency) -> None:
        doctors = await self.db_repository.get_doctors()
        if not doctors:
            # TODO: Handle when there is no doctor at all
            return

        results = await asyncio.gather(
            self.db_repository.get_visitor(emergency.visitor_id),
            self.db_repository.get_gate(emergency.visitor_id),
            self._preprocess_doctors(doctors),
        )
        patient, patient_gate, doctors_by_gates = results[0], results[1], results[2]
        patient_seat = patient.section_seat.split("_")[1]
        nearest_doctors = doctors_by_gates
        # nearest_doctors = await self._find_nearest_doctors(patient_gate, doctors_by_gates)
        await asyncio.gather(
            *(self.fcm_repository.send_message(
                doctor_token,
                DoctorMessage(
                    emergency_code=emergency.emergency_code,
                    from_gate=doctor_gate,
                    to_gate=patient_gate,
                    patient_section=patient.section,
                    patient_seat=patient_seat
                )
            ) for doctor_token, doctor_gate in nearest_doctors)
        )
        # TODO: Send messages to nearby visitors to back off
