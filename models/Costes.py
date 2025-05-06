from sqlmodel import SQLModel, Field

class Costes(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    empleats: int
    eines: int
    productes: int
    factures: int
    coste_total: int