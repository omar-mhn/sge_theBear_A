from sqlmodel import SQLModel, Field

#--------------------------------taula-Producte_final--------------------------------------------------#
class Producte_final(SQLModel, table=True):
    id_producto_fin: int = Field(default=None, primary_key=True)
    nombre: str
    tipo: str
    precio: float
    id_comanda: int = Field(default=None, foreign_key="comanda.id_comanda")
#-----------------------------final-taula-Producte_final--------------------------------------------------#