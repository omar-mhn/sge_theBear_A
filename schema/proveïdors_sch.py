#--------------------------------taula-Proveïdor--------------------------------------------------#

def proveïdor_schema(proveïdor) -> dict:
    response = {"proveïdor": proveïdor}
    return response

def proveïdors_schema(proveïdors) -> list[dict]:
    response = [proveïdor_schema(proveïdor) for proveïdor in proveïdors]
    return response

#-----------------------------final-taula-Proveïdor------------------------------------------------#