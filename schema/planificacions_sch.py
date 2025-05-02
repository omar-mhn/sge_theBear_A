#--------------------------------taula-Planificacio--------------------------------------------------#
def planificacio_schema(planificacio) -> dict:
    response = {"planificacio": planificacio}
    return response

def planificacions_schema(planificacions) -> list[dict]:
    response = [planificacio_schema(planificacio) for planificacio in planificacions]
    return response
#-----------------------------final-taula-Planificacio------------------------------------------------#
