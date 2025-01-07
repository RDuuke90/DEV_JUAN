from abc import ABC, abstractmethod
from typing import List

from app.core.entities import Miner


class MinerRepositoryPort(ABC):

    @abstractmethod
    async def create_miner(self, miner: Miner) -> None:
        raise NotImplemented
    
    @abstractmethod
    async def get_miners(self) -> List[Miner]:
        raise NotImplemented

    @abstractmethod
    async def update_miner(self, miner: Miner) -> None:
        raise NotImplemented
    
    @abstractmethod
    async def delete_miner(self, miner_id: str) -> None:
        raise NotImplemented
    