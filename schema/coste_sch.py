def coste_schema(coste) -> dict:
    response = {"coste": coste}
    return response

def costes_schema(costes) -> list[dict]:
    response = [coste_schema(coste) for coste in costes]
    return response
