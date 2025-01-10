from abc import ABC, abstractmethod
from typing import List

from backend.src.core.miners.domain.entities.miner import Miner


class MinerRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Miner]:
        raise NotImplementedError
