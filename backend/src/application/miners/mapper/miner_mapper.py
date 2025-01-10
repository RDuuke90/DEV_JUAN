from backend.src.application.miners.dtos.miner_response_dto import MinerResponseDTO
from backend.src.core.miners.domain.entities.miner import Miner


class MinerMapper:

    @staticmethod
    def entity_to_dto(miner: Miner) -> MinerResponseDTO:
        return MinerResponseDTO(
            uuid=miner.uuid,
            name=miner.name,
            document_type=miner.document_type,
            document_number=miner.document_number,
            municipality=miner.municipality
        )
