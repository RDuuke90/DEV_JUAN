from pydantic import BaseModel
from pydantic import UUID4


class MinerResponseDTO(BaseModel):
    uuid: UUID4
    name: str
    document_type: str
    document_number: str
    municipality: str
