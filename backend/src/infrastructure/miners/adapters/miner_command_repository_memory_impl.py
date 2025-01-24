from src.core.miners.domain.entities.miner import Miner
from src.infrastructure.miners.persistence.models.miner import MinerModel
from src.core.miners.domain.interfaces.miner_command_repository import MinerCommandRepository


class MinerCommandRepositoryMemoryImpl(MinerCommandRepository):

    def __init__(self):
        self.model = MinerModel()

    async def create(self, miner: Miner) -> None:
        print(miner)
        await self.model.create(**miner.to_dict())