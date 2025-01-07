from typing import List
from uuid import uuid4

from sqlalchemy import delete, insert, select, update
from app.adapters import database
from app.adapters.database.repository import MinerRepositoryPort
from app.core.entities import Miner
from app.adapters.database.model import miners


class MinerRespository(MinerRepositoryPort):

    async def create_miner(self, miner: Miner) -> None:
        query = insert(miners).values(
            id=uuid4(),
            full_name=miner.full_name,
            id_type=miner.id_type,
            id_number=miner.id_number,
            municipality=miner.municipality,
        ).returning(miners)

        await database.fetch_one(query)


    async def get_miners(self) -> List[Miner]:
        query = select(miners)
        results = await database.fetch_all(query)
        return [Miner(**result) for result in results]
    

    async def update_miner(self, miner: Miner) -> None:
        query = update(miners).where(miners.c.id == miner.id).values(
            full_name=miner.full_name,
            id_type=miner.id_type,
            id_number=miner.id_number,
            municipality=miner.municipality,
        ).returning(miners)

        await database.fetch_one(query)


    async def delete_miner(self, miner_id: str) -> None:
        query = delete(miners).where(miners.c.id == miner_id)
        await database.execute(query)