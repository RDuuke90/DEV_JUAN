from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.entrypoints.rest_api.router import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router=router, prefix="/api/v1")

register_tortoise(
    app,
    db_url="sqlite://miners.db",
    modules={"models": ["src.infrastructure.miners.persistence.models.miner"]},
    generate_schemas=True,
    add_exception_handlers=True,
)