import React, { useState } from 'react';
import { createMiner } from '../services/minerService';
import { Miner } from '../interfaces/Miner';

const CreateMiner: React.FC = () => {
  const [miner, setMiner] = useState<Omit<Miner, 'id'>>({
    full_name: '',
    id_type: '',
    id_number: '',
    municipality: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setMiner({ ...miner, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createMiner(miner);
      alert('Minero creado exitosamente');
    } catch (error) {
      console.error('Error creando minero:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="full_name" placeholder="Nombre completo" onChange={handleChange} />
      <select name="id_type" onChange={handleChange}>
        <option value="CC">Cédula de Ciudadanía</option>
        <option value="TI">Tarjeta de Identidad</option>
      </select>
      <input name="id_number" placeholder="Número de identificación" onChange={handleChange} />
      <input name="municipality" placeholder="Municipio" onChange={handleChange} />
      <button type="submit">Crear Minero</button>
    </form>
  );
};

export default CreateMiner;
