from typing import List, Dict

from src.core.miners.domain.entities.miner import Miner
from src.core.miners.domain.interfaces.miner_query_repository import MinerQueryRepository
from src.infrastructure.miners.persistence.models.miner import MinerModel


class MinerQueryRepositoryMemoryImplement(MinerQueryRepository):

    def __init__(self):
        self.model = MinerModel()

    async def get_all(self) -> List[Miner]:
        miners:List[Dict] = await self.model.all().values()
        return [Miner.from_dict(miner) for miner in miners]
