
from sqlmodel import SQLModel,Field


class Reunio(SQLModel,table=True):
    id_reunio:int=Field(default=None,primary_key=True)
    data : str
    informacio : str
    nom_eseveniment : str

