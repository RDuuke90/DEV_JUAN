from abc import ABC, abstractmethod
from src.core.miners.domain.entities.miner import Miner


class MinerCommandRepository(ABC):

    @abstractmethod
    async def create(self, miner: Miner) -> None:
        raise NotImplementedError
