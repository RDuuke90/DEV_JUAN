import {Miner} from "../models/Miner.ts"
import {MinerDTO} from "../dtos/MinerResponseDTO.ts";

export class MinerMapper {

    static fromDTO(dto: MinerDTO) : Miner
    {
        return {
            uuid: dto.uuid,
            name: dto.name,
            documentType: dto.document_type,
            documentNumber: dto.document_number,
            municipality: dto.municipality
        }
    }

    static toDTO(miner: Miner) : MinerDTO
    {
        return {
            uuid: miner.uuid,
            name: miner.name,
            document_type: miner.documentType,
            document_number: miner.documentNumber,
            municipality: miner.municipality
        }
    }
}