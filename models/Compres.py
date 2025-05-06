from sqlmodel import SQLModel, Field

class Compres(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    provedor: str
    productos: str
    cantidad_producto: int
    precio_producto: int
    precio_total: int
