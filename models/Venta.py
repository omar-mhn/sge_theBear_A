from sqlmodel import SQLModel, Field

#---------------------------Taula-Venta---------------------------#

class Venta(SQLModel, table=True):
    id_venta: int = Field(default=None, primary_key=True)
    cost_total: int
    data_comanda: str

#---------------------------Taula-Venta_final---------------------------#