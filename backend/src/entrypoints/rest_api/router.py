from typing import List

from fastapi import APIRouter

from src.application.miners.dtos.miner_response_dto import MinerResponseDTO
from src.entrypoints.rest_api.miner_controller import MinerController

from src.application.miners.dtos.miner_create_dto import MinerCreateDTO

router = APIRouter()

@router.get("/miners", response_model=List[MinerResponseDTO])
async def action_list_miners():
    return await MinerController().get_miners()

@router.post("/miners")
async def action_create_miner(miner_dto: MinerCreateDTO):
    await MinerController().create(dto=miner_dto)
