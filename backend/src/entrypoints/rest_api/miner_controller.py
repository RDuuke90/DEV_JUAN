from typing import List

from src.application.miners.dtos.miner_response_dto import MinerResponseDTO
from src.application.miners.mapper.miner_mapper import MinerMapper
from src.core.miners.domain.entities.miner import Miner
from src.core.miners.use_cases.query.list_miners import ListMinersQuery
from src.infrastructure.miners.adapters.miner_query_repository_memory_impl import MinerQueryRepositoryMemoryImplement

from src.application.miners.dtos.miner_create_dto import MinerCreateDTO
from src.core.miners.use_cases.command.create_miner import CreateMinersCommand
from src.infrastructure.miners.adapters.miner_command_repository_memory_impl import \
    MinerCommandRepositoryMemoryImpl

miner_query_repository = MinerQueryRepositoryMemoryImplement()
list_miners_use_case = ListMinersQuery(repository=miner_query_repository)
miner_command_repository = MinerCommandRepositoryMemoryImpl()
create_miners_use_case = CreateMinersCommand(repository=miner_command_repository)

class MinerController:

    @staticmethod
    async def get_miners() -> List[MinerResponseDTO]:
        miners: List[Miner] = await list_miners_use_case.execute()
        return [MinerMapper.entity_to_dto(miner=miner) for miner in miners]


    @staticmethod
    async def create(dto: MinerCreateDTO) -> None:
        await create_miners_use_case.execute(miner=dto)
