#--------------------------------taula-Client--------------------------------------------------#
def client_schema(client) -> dict:
    response = {"client": client}
    return response

def clients_schema(clients) -> list[dict]:
    response = [client_schema(client) for client in clients]
    return response
#-----------------------------final-taula-Client------------------------------------------------#
