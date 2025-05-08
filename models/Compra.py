from sqlmodel import SQLModel, Field

class Compra(SQLModel, table=True):
    id_compra: int = Field(default=None, primary_key=True)
    proveïdor: str
    productes: str
    quantitat_producte: int
    preu_producte: int
    preu_total: int
    data_compra: str