from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from server.api.dependencies import get_visitors_service
from server.schemas.visitors import UpdateTokenRequest
from server.schemas.visitors import Visitor
from server.schemas.visitors import VisitorResponse
from server.services.visitors_service import VisitorsService

router = APIRouter(prefix="/visitors")


@router.put("/register", status_code=status.HTTP_201_CREATED, response_model=VisitorResponse)
async def register_visitor(
    visitor: Visitor,
    visitors_service: VisitorsService = Depends(get_visitors_service)
) -> VisitorResponse:
    response = await visitors_service.register_visitor(visitor)
    if response.visitor_id == -1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Visitor already exists")
    return response


@router.get("/{visitor_id}", status_code=status.HTTP_200_OK, response_model=Visitor)
async def get_visitor(visitor_id: int, visitors_service: VisitorsService = Depends(get_visitors_service)) -> Visitor:
    visitor = await visitors_service.get_visitor(visitor_id)
    if not visitor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Visitor does not exist")
    return visitor


@router.post("/update_token", status_code=status.HTTP_202_ACCEPTED, response_model=VisitorResponse)
async def update_token(
    update_token_request: UpdateTokenRequest,
    visitors_service: VisitorsService = Depends(get_visitors_service)
) -> VisitorResponse:
    response = await visitors_service.update_token(update_token_request)
    if response.visitor_id == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Visitor does not exist")
    return response
