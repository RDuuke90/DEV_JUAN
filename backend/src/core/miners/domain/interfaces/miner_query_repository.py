from abc import ABC, abstractmethod
from typing import List

from src.core.miners.domain.entities.miner import Miner


class MinerQueryRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Miner]:
        raise NotImplementedError
