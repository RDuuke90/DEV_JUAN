import {Miner} from "../models/Miner.ts"
import {MinerResponseDTO} from "../dtos/MinerResponseDTO.ts";

export class MinerMapper {

    static fromDTO(dto: MinerResponseDTO) : Miner
    {
        return {
            uuid: dto.uuid,
            name: dto.name,
            documentType: dto.document_type,
            documentNumber: dto.document_number,
            municipality: dto.municipality
        }
    }
}