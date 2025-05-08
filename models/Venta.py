from sqlmodel import SQLModel, Field

class Venta(SQLModel, table=True):
    id_venta: int = Field(default=None, primary_key=True)
    cost_total: int
    data_comanda: str
