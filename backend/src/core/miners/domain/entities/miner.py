from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class Miner:
    uuid: UUID
    name: str
    document_type: str
    document_number: str
    municipality: str
    updated_at: Optional[datetime] = None

    @classmethod
    def create(cls, data: dict) -> "Miner":
        return cls(
            uuid=uuid4(),
            name=data.get("name"),
            document_type=data.get("document_type"),
            document_number=data.get("document_number"),
            municipality=data.get("municipality"),
        )

    def to_dict(self) -> dict:
        return {
            "uuid": str(self.uuid),
            "name": self.name,
            "document_type": self.document_type,
            "document_number": self.document_number,
            "municipality": self.municipality,
            "updated_at": self.updated_at
        }
