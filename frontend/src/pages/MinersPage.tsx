import * as React from "react";
import MinerList from "../components/MinerList.tsx";

const MinersPage: React.FC = () => {
    return (
        <div>
            <h1>Miners</h1>
            <MinerList />
        </div>
    )
}

export default MinersPage;