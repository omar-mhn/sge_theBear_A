from sqlmodel import SQLModel, Field

#--------------------------------taula-Crear--------------------------------------------------#
class Crear(SQLModel, table=True):
    id_prestatgeria: int = Field(default=None, primary_key=True)
    id_producto_fin: int = Field(default=None, primary_key=True)
#-----------------------------final-taula-Comanda--------------------------------------------------#