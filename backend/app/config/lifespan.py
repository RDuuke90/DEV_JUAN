from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.config.database import metadata, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

    yield

    await engine.dispose()