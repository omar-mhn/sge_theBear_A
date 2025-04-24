from enum import Enum
from sqlmodel import SQLModel, Field

class EmpleatRol(str, Enum):
    MANAGER = "manager"
    CHEF = "chef"
    WAITER = "waiter"
    CASHIER = "cashier"


class Empleat(SQLModel, table=True):
    EmpleatId: int = Field(default=None, primary_key=True)
    Nom: str
    Email: str
    Telefon: int
    Adreca: str
    Rol: EmpleatRol

