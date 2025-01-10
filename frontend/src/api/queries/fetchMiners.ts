import { MinerResponseDTO } from "../../dtos/MinerResponseDTO";
import apiClient from "../apiClient"


export const fetchMiners = async (): Promise<MinerResponseDTO[]> => {
    const response = await apiClient.get<MinerResponseDTO[]>("/miners");
    return response.data;
}
