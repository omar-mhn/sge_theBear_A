from enum import Enum
from sqlmodel import SQLModel, Field

class Empleat(SQLModel, table=True):
    EmpleatId: str = Field(default=None, primary_key=True)
    Nom: str
    Email: str
    Telefon: str
    Adreca: str
    Rol: str

