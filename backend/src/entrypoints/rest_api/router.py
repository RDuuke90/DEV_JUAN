from typing import List

from fastapi import APIRouter

from src.application.miners.dtos.miner_response_dto import MinerResponseDTO
from src.entrypoints.rest_api.miner_controller import MinerController

router = APIRouter()

@router.get("/miners", response_model=List[MinerResponseDTO])
async def action_list_miners():
    return await MinerController().get_miners()