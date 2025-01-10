from typing import List
from uuid import uuid4

from backend.src.core.miners.domain.entities.miner import Miner
from backend.src.core.miners.domain.interfaces.miner_query_repository import MinerQueryRepository


class MinerQueryRepositoryMemoryImplement(MinerQueryRepository):

    def __init__(self):
        self.miners: List[Miner] = [
            Miner(
                uuid=uuid4(),
                name="Juan Perez",
                document_type="CC",
                document_number="123456789",
                municipality="Medellin"
            ),
            Miner(
                uuid=uuid4(),
                name="Ana Gomez",
                document_type="CC",
                document_number="987654321",
                municipality="Bogota"
            )
        ]

    async def get_all(self) -> List[Miner]:
        return self.miners
