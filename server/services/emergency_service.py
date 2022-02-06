from collections import defaultdict
from collections import deque
from typing import Dict
from typing import List

import asyncio

from server.repositories.fcm_repository import FCMRepository
from server.repositories.visitors_repository import VisitorsRepository
from server.schemas.emergency import Emergency
from server.schemas.visitors import Doctor

# TODO: Initialize graph
graph = dict()


class EmergencyService:
    def __init__(self, visitors_repository: VisitorsRepository, fcm_repository: FCMRepository):
        self.visitors_repository = visitors_repository
        self.fcm_repository = fcm_repository

    @classmethod
    async def _preprocess_doctors(cls, doctors: List[Doctor]) -> Dict[int, List[str]]:
        doctors_by_gates = defaultdict(list)
        for doctor in doctors:
            doctors_by_gates[doctor.gate].append(doctor.fcm_token)
        return doctors_by_gates

    @classmethod
    async def _find_nearest_doctors(
        cls,
        patient_gate: int,
        doctors: Dict[int, List[str]],
        num_doctors: int = 3
    ) -> List[str]:
        queue = deque([patient_gate])
        visited = {patient_gate}
        doctor_tokens = []
        while queue:
            gate = queue.popleft()
            gate_tokens = doctors[gate]
            doctor_tokens.extend(gate_tokens)
            if len(doctor_tokens) >= num_doctors:
                return doctor_tokens[:num_doctors]
            for neighbor_gate in graph[gate]:
                if neighbor_gate not in visited:
                    visited.add(neighbor_gate)
                    queue.append(neighbor_gate)
        return doctor_tokens

    async def handle_emergency(self, emergency: Emergency) -> None:
        results = await asyncio.gather(
            self.visitors_repository.get_doctors(),
            self.visitors_repository.get_visitor(emergency.visitor_id)
        )
        doctors, patient_gate = results[0], results[1]
        if not doctors:
            # TODO: Handle when there is no doctor at all
            return
        doctors_by_gates = await self._preprocess_doctors(doctors)
        doctor_tokens = await self._find_nearest_doctors(patient_gate, doctors_by_gates)
        await self.fcm_repository.multicast_message(doctor_tokens)
        # TODO: Send messages to nearby visitors to back off
