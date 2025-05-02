from sqlmodel import SQLModel, Field

#--------------------------------taula-Coste--------------------------------------------------#
class Coste(SQLModel, table=True):
    id_factura: int = Field(default=None, primary_key=True)
    data: str
    tipus_cost: str
    cost_total: str
    id_compra: int = Field(default=None, foreign_key="compra.id_compra")
    id_empleat: int = Field(default=None, foreign_key="empleat.id_empleat")
    id_comanda: int  = Field(default=None, foreign_key="comanda.id_comanda")

#-----------------------------final-taula-Coste--------------------------------------------------#