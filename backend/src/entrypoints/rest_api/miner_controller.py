from typing import List

from src.application.miners.dtos.miner_response_dto import MinerResponseDTO
from src.application.miners.mapper.miner_mapper import MinerMapper
from src.core.miners.domain.entities.miner import Miner
from src.core.miners.use_cases.query.list_miners import ListMinersQuery
from src.infrastructure.miners.adapters.miner_query_repository_memory_impl import MinerQueryRepositoryMemoryImplement

miner_query_repository = MinerQueryRepositoryMemoryImplement()
list_miners_use_case = ListMinersQuery(repository=miner_query_repository)

class MinerController:

    @staticmethod
    async def get_miners() -> List[MinerResponseDTO]:
        miners: List[Miner] = await list_miners_use_case.execute()
        return [MinerMapper.entity_to_dto(miner=miner) for miner in miners]
