from sqlmodel import SQLModel, Field

#--------------------------------taula-Planificacio--------------------------------------------------#
class Planificacio(SQLModel, table=True):
    id_horari: int = Field(default=None, primary_key=True)
    data: str
    horari: int
    rol: str
    id_empleat: int = Field(default=None, foreign_key="empleat.id_empleat")
#-----------------------------final-taula-Planificacio--------------------------------------------------#