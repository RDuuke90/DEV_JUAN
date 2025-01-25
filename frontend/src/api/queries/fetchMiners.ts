import { MinerDTO } from "../../dtos/MinerResponseDTO";
import apiClient from "../apiClient"


export const fetchMiners = async (): Promise<MinerDTO[]> => {
    const response = await apiClient.get<MinerDTO[]>("/miners");
    return response.data;
}
