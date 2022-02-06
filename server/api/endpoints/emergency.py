from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from server.api.dependencies import get_emergency_service
from server.schemas.emergency import Emergency
from server.services.emergency_service import EmergencyService

router = APIRouter(prefix="/emergency")


@router.post("", status_code=status.HTTP_202_ACCEPTED)
async def detect_emergency(
    emergency: Emergency,
    emergency_service: EmergencyService = Depends(get_emergency_service)
) -> None:
    if not await emergency_service.handle_emergency(emergency):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Visitor does not exist")
