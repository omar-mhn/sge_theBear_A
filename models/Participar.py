from sqlmodel import SQLModel, Field

#--------------------------------taula-Participar--------------------------------------------------#
class Participar(SQLModel, table=True):
    id_empleat: int = Field(primary_key=True)
    id_reunio: int = Field(primary_key=True)
    id_proveidor: int = Field(primary_key=True)
#-----------------------------final-taula-Participar-----------------------------------------------#