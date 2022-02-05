from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.api.dependencies import get_settings

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
