from fastapi import APIRouter

from app.core.entities import Miner
from app.core.use_cases import MinerUseCase
from app.interfaces.repository import MinerRespository


api_router = APIRouter()
repository = MinerRespository()
use_case = MinerUseCase(repository=repository)

@api_router.get("/miners")
async def get_miners():
    return await use_case.get_miners()

@api_router.post("/miners")
async def create_miner(miner: Miner):
    return await use_case.create_miner(miner)

@api_router.put("/miners")
async def update_miner(miner: Miner):
    return await use_case.update_miner(miner)

@api_router.delete("/miners/{miner_id}")
async def delete_miner(miner_id: str):
    return await use_case.delete_miner(miner_id)
