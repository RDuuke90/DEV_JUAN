from fastapi import FastAPI

from backend.src.entrypoints.rest_api.router import router

app = FastAPI()

app.include_router(router=router, prefix="/api/v1")

