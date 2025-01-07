import api from '../api/axios';
import { Miner } from '../interfaces/Miner';

export const getAllMiners = async (): Promise<Miner[]> => {
  const response = await api.get<Miner[]>('/miners');
  return response.data;
};

export const getMinerById = async (id: string): Promise<Miner> => {
  const response = await api.get<Miner>(`/miners/${id}`);
  return response.data;
};

export const createMiner = async (miner: Omit<Miner, 'id'>): Promise<Miner> => {
  const response = await api.post<Miner>('/miners', miner);
  return response.data;
};

export const updateMiner = async (id: string, miner: Partial<Miner>): Promise<Miner> => {
  const response = await api.put<Miner>(`/miners/${id}`, miner);
  return response.data;
};

// Eliminar un minero
export const deleteMiner = async (id: string): Promise<void> => {
  await api.delete(`/miners/${id}`);
};
