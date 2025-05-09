from sqlmodel import SQLModel, Field

#--------------------------------taula-Proveidor---------------------------#

class Proveidor(SQLModel, table=True):
    Nom: str
    telefòn: str
    email: str
    id_proveidor: int = Field(default=None, primary_key=True)
    informaciò: str
# --------------------------------taula-Proveidor_final-----------------------#




