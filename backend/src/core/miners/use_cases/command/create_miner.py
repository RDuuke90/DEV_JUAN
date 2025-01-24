from src.core.miners.domain.entities.miner import Miner
from src.core.miners.domain.interfaces.miner_command_repository import MinerCommandRepository

from src.application.miners.dtos.miner_create_dto import MinerCreateDTO


class CreateMinersCommand:

    def __init__(self, repository: MinerCommandRepository):
        self.repository = repository


    async def execute(self, miner: MinerCreateDTO) -> None:
        miner: Miner = Miner.create(data=miner.dict())
        await self.repository.create(miner=miner)
