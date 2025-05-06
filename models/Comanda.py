from sqlmodel import SQLModel, Field

#--------------------------------taula-Comanda--------------------------------------------------#
class Comanda(SQLModel, table=True):
    id_comanda: int = Field(default=None, primary_key=True)
    n_taula: int
    quantitat: int
    producte: str
    data: str
    id_client: int = Field(default=None, foreign_key="client.id_client")
#-----------------------------final-taula-Comanda--------------------------------------------------#