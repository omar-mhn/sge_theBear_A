from datetime import date
from sqlmodel import SQLModel,Field


class Pedido (SQLModel,table=True):
    id_pedido :int=Field(default=None,primary_key=True)
    cantidad : int
    precio : float
    product: str
    fecha : date
    empleat_id : int = Field(foreign_key= "empleado.id_empleado") # todavia no tenemos empleado 

