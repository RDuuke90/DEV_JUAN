from dataclasses import dataclass
from typing import Optional


@dataclass 
class Miner:
    id: Optional[str] = None 
    full_name: str
    id_type: str
    id_document: str
    minucipality: str

