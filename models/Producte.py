
from sqlmodel import SQLModel,Field


class Producte(SQLModel,table=True):
    id_producte:str=Field(default=None,primary_key=True)
    cost : str
    quantitat : str
    nom_producte : str
    id_proveidor: str = Field(default=None, foreign_key="proveidor.Id_proveidor")
    id_prestatgeria: str = Field(default=None, foreign_key="prestatgeria.Id_prestatgeria")

