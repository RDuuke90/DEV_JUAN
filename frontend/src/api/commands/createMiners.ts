import { MinerDTO } from "../../dtos/MinerResponseDTO";
import apiClient from "../apiClient"


export const createMiners = async (miner:MinerDTO) => {
    try {
        const response = await apiClient.post("/miners", miner);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}
