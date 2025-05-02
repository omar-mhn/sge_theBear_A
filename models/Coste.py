from sqlmodel import SQLModel, Field


class Coste(SQLModel, table=True):
    id_factura: str = Field(default=None, primary_key=True)
    data: str
    tipus_cost: str
    cost_total: str
    id_compra: str = Field(default=None, foreign_key="compra.id_compra")
    id_empleat: str = Field(default=None, foreign_key="empleat.id_empleat")
    id_comanda: str = Field(default=None, foreign_key="comanda.id_comanda")
