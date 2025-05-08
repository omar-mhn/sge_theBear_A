from sqlmodel import SQLModel, Field

class Proveïdor(SQLModel, table=True):
    id_proveïdor: int = Field(default=None, primary_key=True)
    email: str
    telefòn: str
    Nom: str
    informaciò: str




