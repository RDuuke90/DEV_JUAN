import React from 'react';
import { deleteMiner } from '../services/minerService';

const DeleteMiner: React.FC<{ id: string }> = ({ id }) => {
  const handleDelete = async () => {
    try {
      await deleteMiner(id);
      alert('Minero eliminado exitosamente');
    } catch (error) {
      console.error('Error eliminando minero:', error);
    }
  };

  return <button onClick={handleDelete}>Eliminar Minero</button>;
};

export default DeleteMiner;
