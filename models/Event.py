import datetime
from sqlmodel import SQLModel, Field

class Reserva(SQLModel, table=True):
    reservaId: int = Field(default=None, primary_key=True)
    Nom: str
    Estat: str
    numPersona: int
    Telefon: int
    Data: datetime