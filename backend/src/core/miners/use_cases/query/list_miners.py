from typing import List

from src.core.miners.domain.entities.miner import Miner
from src.core.miners.domain.interfaces.miner_query_repository import MinerQueryRepository


class ListMinersQuery:

    def __init__(self, repository: MinerQueryRepository):
        self.repository = repository


    async def execute(self) -> List[Miner]:
        return await self.repository.get_all()
