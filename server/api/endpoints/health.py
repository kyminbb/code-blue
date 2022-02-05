from fastapi import APIRouter
from starlette.responses import Response
from starlette.status import HTTP_200_OK

router = APIRouter()


@router.get("/health", status_code=HTTP_200_OK, response_class=Response)
async def health():
    pass
