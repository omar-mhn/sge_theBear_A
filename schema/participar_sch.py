#--------------------------------taula-Participar--------------------------------------------------#
def participacio_schema(participacio) -> dict:
    response = {"participacio":participacio}
    return response

def participacions_schema(participacions) -> list[dict]:
    response = [participacio_schema(participacio) for participacio in participacions]
    return response
#--------------------------------taula-Participar--------------------------------------------------#