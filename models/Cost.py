from sqlmodel import SQLModel, Field

class Cost(SQLModel, table=True):
    id_cost: int = Field(default=None, primary_key=True)
    empleats: int
    eines: int
    productes: int
    factures: int
    cost_total: int
    data_cost: str