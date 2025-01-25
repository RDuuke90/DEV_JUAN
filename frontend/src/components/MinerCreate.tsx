import { useState } from "react";
import { Miner } from "../models/Miner";
import { createMiners } from "../api/commands/createMiners";
import { MinerMapper } from "../mappers/minerMapper";

const CreateMinerForm = () => {
    const [formData, setFormData] = useState<Miner>({
        uuid: "",
        name: "",
        documentNumber: "",
        municipality: "",
        documentType: ""
    });

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        
        setFormData((prev) => ({...prev, [name]: value}));
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        try {
            await createMiners(MinerMapper.toDTO(formData));
            setFormData({
                uuid: "",
                name: "",
                documentNumber: "",
                municipality: "",
                documentType: ""
            })
        } catch (error) {
            console.log("Error creating miner");
        }
    };

    return (
        <div>
          <h1>Create Miner</h1>
          <form onSubmit={handleSubmit}>
            <div>
              <label>Name:</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label>Document Type:</label>
              <input
                type="text"
                name="documentType"
                value={formData.documentType}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label>Document Number:</label>
              <input
                type="text"
                name="documentNumber"
                value={formData.documentNumber}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label>Municipality:</label>
              <input
                type="text"
                name="municipality"
                value={formData.municipality}
                onChange={handleChange}
                required
              />
            </div>
            <button type="submit">Create</button>
          </form>
        </div>
      );
    };
    
    export default CreateMinerForm;
