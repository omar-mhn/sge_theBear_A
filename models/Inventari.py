from sqlmodel import SQLModel, Field

#--------------------------------taula-Inventari--------------------------------------------------#
class Inventari(SQLModel, table=True):
    id_estanteria: int = Field(default=None, primary_key=True)
    nombre_materia_prima: str
    cantidad_min: int
    fecha_entrada: str
    fecha_caducidad: str
    stock: int
#-----------------------------final-taula-Inventari-----------------------------------------------#
