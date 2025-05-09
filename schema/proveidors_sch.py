#--------------------------------taula-Proveidor--------------------------------------------------#

def proveidor_schema(proveidor) -> dict:
    response = {"proveidor": proveidor}
    return response

def proveidors_schema(proveidors) -> list[dict]:
    response = [proveidor_schema(proveidor) for proveidor in proveidors]
    return response

#-----------------------------final-taula-Proveidor------------------------------------------------#