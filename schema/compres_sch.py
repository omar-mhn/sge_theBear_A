#--------------------------------taula-Compra--------------------------------------------------#
def compra_schema(compra) -> dict:
    response = {"compra": compra}
    return response

def compres_schema(compres) -> list[dict]:
    response = [compra_schema(compra) for compra in compres]
    return response

#-----------------------------final-taula-Compra------------------------------------------------#