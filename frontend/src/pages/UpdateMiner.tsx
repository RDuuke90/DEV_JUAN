import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getMinerById, updateMiner } from '../services/minerService';
import { Miner } from '../interfaces/Miner';

const UpdateMiner: React.FC = () => {
  const { id } = useParams<{ id: string }>(); // Obtener el id desde la URL
  const [miner, setMiner] = useState<Partial<Miner>>({
    full_name: '',
    municipality: '',
  });

  useEffect(() => {
    const fetchMiner = async () => {
      if (id) {
        try {
          const minerData = await getMinerById(id);
          setMiner(minerData);
        } catch (error) {
          console.error('Error fetching miner:', error);
        }
      }
    };

    fetchMiner();
  }, [id]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setMiner({ ...miner, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      if (id) {
        await updateMiner(id, miner);
        alert('Minero actualizado exitosamente');
      }
    } catch (error) {
      console.error('Error actualizando minero:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="full_name"
        value={miner.full_name || ''}
        placeholder="Nombre completo"
        onChange={handleChange}
      />
      <input
        name="municipality"
        value={miner.municipality || ''}
        placeholder="Municipio"
        onChange={handleChange}
      />
      <button type="submit">Actualizar Minero</button>
    </form>
  );
};

export default UpdateMiner;
