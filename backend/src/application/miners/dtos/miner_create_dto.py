from typing import Dict

from pydantic import BaseModel, Field


class MinerCreateDTO(BaseModel):
    name: str = Field(..., examples="Juan Carlos")
    document_type: str = Field(..., examples="CC")
    document_number: str = Field(..., examples="123456789")
    municipality: str = Field(..., examples="Medellín")

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "document_type": self.document_type,
            "document_number": self.document_number,
            "municipality": self.municipality,
        }
