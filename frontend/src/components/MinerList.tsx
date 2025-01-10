import * as React from "react";
import {useEffect, useState} from "react";
import {Miner} from "../models/Miner.ts";
import {fetchMiners} from "../api/queries/fetchMiners.ts";
import {MinerMapper} from "../mappers/minerMapper.ts";

const MinerList: React.FC = () => {
    const [miners, setMiners] = useState<Miner[]>([]);
    const [loading, setLoading] = useState<boolean>(true)

    useEffect(() => {
        const loadMiners = async () => {
            try {
                const minersDTO = await fetchMiners()
                const miners = minersDTO.map(MinerMapper.fromDTO)
                setMiners(miners)
            } catch (error) {
                console.log("Error fetching miners:", error)
            } finally {
                setLoading(false)
            }
        }

        loadMiners()

    }, [])

    if (loading) {
        return <p>Loadings miners...</p>
    }

    return (
        <div>
            <h2>Lista de Mineros</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Documento</th>
                        <th>Municipio</th>
                    </tr>
                </thead>
                <tbody>
                {
                    miners.map((miner) => { return (
                        <tr key={miner.uuid}>
                            <td>
                                {miner.uuid}
                            </td>
                            <td>
                                {miner.name}
                            </td>
                            <td>
                                {miner.documentNumber}
                            </td>
                            <td>
                                {miner.municipality}
                            </td>
                        </tr>
                    )
                })}
                </tbody>
            </table>
        </div>
    )
}

export default MinerList;