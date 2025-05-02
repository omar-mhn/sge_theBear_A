from enum import Enum
from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    id_client: int = Field(default=None, primary_key=True)
    nom: str
    email: str
    telefon: str
