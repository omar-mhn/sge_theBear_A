from sqlmodel import SQLModel, Field
from typing import Optional

#--------------------------------taula-Client--------------------------------------------------#
class Client(SQLModel, table=True):
    id_client: int = Field(default=None, primary_key=True)
    nom: str
    email: Optional[str] = Field(default=None)
    telefon: Optional[str] = Field(default=None)
#-----------------------------final-taula-Client-----------------------------------------------#
