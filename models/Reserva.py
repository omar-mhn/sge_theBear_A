import datetime
from sqlmodel import SQLModel, Field
#--------------------------------TAULA-RESERVA--------------------------------------------------#
class Reserva(SQLModel, table=True):
    id_reserva: int = Field(default=None, primary_key=True)
    nom: str
    estat: str
    numPersona: int
    telefon: str
    data: str
    id_client: int = Field(default=None, foreign_key="client.id_client")
#--------------------------------TAULA-RESERVA--------------------------------------------------#