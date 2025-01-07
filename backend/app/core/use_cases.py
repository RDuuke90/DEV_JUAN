from typing import List
from app.adapters.database.repository import MinerRepositoryPort
from app.core.entities import Miner


class MinerUseCase:
    
    def __init__(self, repository: MinerRepositoryPort):
        self.repository = repository

    def get_miners(self) -> List[Miner]:
        return self.repository.get_miners()

    def create_miner(self, miner: Miner) -> Miner:
        return self.repository.create_miner(miner)

    def update_miner(self, miner: Miner) -> Miner:
        return self.repository.update_miner(miner)

    def delete_miner(self, miner_id: str) -> None:
        return self.repository.delete_miner(miner_id)