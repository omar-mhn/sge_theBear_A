#--------------------------------taula-Crear--------------------------------------------------#
def crear_schema(crear) -> dict:
    response = {"crear": crear}
    return response

def crears_schema(crears) -> list[dict]:
    response = [crear_schema(crear) for crear in crears]
    return response
#-----------------------------final-taula-Crear------------------------------------------------#
