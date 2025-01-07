from fastapi import FastAPI
from app.config import lifespan
from app.adapters.api.router import api_router

app = FastAPI(lifespan=lifespan)

app.include_router(router=api_router, prefix="/api/v1", tags=["Miners"])

