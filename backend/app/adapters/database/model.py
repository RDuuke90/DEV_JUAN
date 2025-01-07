import uuid
from sqlalchemy import Table, Column, String
from app.config.database import metadata
miners = Table(
    "miners",
    metadata,
    Column("id", String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False),
    Column("full_name", String(255), nullable=False),
    Column("id_type", String(50), nullable=False),
    Column("id_number", String(100), unique=True, nullable=False),
    Column("municipality", String(100), nullable=False),
)

