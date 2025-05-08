#--------------------------------taula-Comanda--------------------------------------------------#
def comanda_schema(comanda) -> dict:
    response = {"comanda": comanda}
    return response

def comandes_schema(comandes) -> list[dict]:
    response = [comanda_schema(comanda) for comanda in comandes]
    return response

#-----------------------------final-taula-Comanda------------------------------------------------#