from sqlmodel import SQLModel, Field

#--------------------------------taula-Producte_final--------------------------------------------------#
class Producte_final(SQLModel, table=True):
    id_producto_fin: int = Field(default=None, primary_key=True)
    nombre: str
    tipo: str
    precio: float
    comandaid: int = Field(default=None, foreign_key="comanda.comandaid")
#-----------------------------final-taula-Producte_final--------------------------------------------------#