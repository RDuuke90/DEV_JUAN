from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class Miner:
    uuid: UUID
    name: str
    document_type: str
    document_number: str
    municipality: str
    updated_at: Optional[datetime] = None
