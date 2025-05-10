from sqlmodel import SQLModel, Field
from decimal import Decimal

#---------------------------Taula-Venta---------------------------#

class Vendre(SQLModel, table=True):
    id_compra: int = Field(default=None, primary_key=True)
    cost_total: Decimal
    data_comanda: str

#---------------------------Taula-Venta_final---------------------------#