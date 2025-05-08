from enum import Enum
from sqlmodel import SQLModel, Field
#--------------------------------TAULA-EMPLEAT--------------------------------------------------#
class Empleat(SQLModel, table=True):
    id_empleat: int = Field(default=None, primary_key=True)
    nom: str
    email: str
    telefon: str
    adreca: str
    rol: str
#--------------------------------TAULA-EMPLEAT--------------------------------------------------#
