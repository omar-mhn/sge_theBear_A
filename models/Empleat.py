from enum import Enum
from sqlmodel import SQLModel, Field

class Empleat(SQLModel, table=True):
    empleatid: str = Field(default=None, primary_key=True)
    nom: str
    email: str
    telefon: str
    adreca: str
    rol: str

