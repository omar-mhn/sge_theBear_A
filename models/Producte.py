
from sqlmodel import SQLModel,Field

#--------------------------------taula-Producte--------------------------------------------------#

class Producte(SQLModel,table=True):
    id_producte:int=Field(default=None,primary_key=True)
    cost : float
    quantitat : int
    nom_producte : str
    #id_proveidor: int = Field(default=None, foreign_key="proveidor.Id_proveidor")
    #id_prestatgeria: int  = Field(default=None, foreign_key="prestatgeria.Id_prestatgeria")

#-----------------------------final-taula-Producte--------------------------------------------------#