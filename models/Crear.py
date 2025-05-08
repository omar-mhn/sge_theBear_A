from sqlmodel import SQLModel, Field

#--------------------------------taula-Crear--------------------------------------------------#
class Crear(SQLModel, table=True):
    id_prestatgeria: int = Field(default=None, primary_key=True)
    id_comanda: int = Field(default=None, foreign_key="comanda.id_comanda")
#-----------------------------final-taula-Comanda--------------------------------------------------#