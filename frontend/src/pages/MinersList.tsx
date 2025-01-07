import React, { useEffect, useState } from 'react';
import { getAllMiners } from '../services/minerService';
import { Miner } from '../interfaces/Miner';

const MinersList: React.FC = () => {
  const [miners, setMiners] = useState<Miner[]>([]);

  useEffect(() => {
    const fetchMiners = async () => {
      try {
        const minersData = await getAllMiners();
        setMiners(minersData);
      } catch (error) {
        console.error('Error fetching miners:', error);
      }
    };

    fetchMiners();
  }, []);

  return (
    <div>
      <h2>Lista de Mineros</h2>
      <ul>
        {miners.map((miner) => (
          <li key={miner.id}>
            {miner.full_name} - {miner.municipality}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MinersList;
