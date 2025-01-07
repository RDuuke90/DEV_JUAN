import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MinersList from './pages/MinersList';
import CreateMiner from './pages/CreateMiner';
import UpdateMiner from './pages/UpdateMiner';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MinersList />} />
        <Route path="/create" element={<CreateMiner />} />
        <Route path="/update/:id" element={<UpdateMiner />} />
      </Routes>
    </Router>
  );
};

export default App;
