import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MinersPage from "./pages/MinersPage.tsx";
import CreateMinerForm from "./components/MinerCreate.tsx";

const App: React.FC = ()  =>{
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MinersPage />} />
        <Route path="/create" element={<CreateMinerForm />} />
      </Routes>
    </Router>
  )
}

export default App
