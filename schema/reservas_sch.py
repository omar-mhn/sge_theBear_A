#--------------------------------taula-reserva--------------------------------------------------#
def reserva_schema(reserva) -> dict:
    response = {"reserva":reserva}
    return response

def reservas_schema(reservas) -> list[dict]:
    response = [reserva_schema(reserva) for reserva in reservas]
    return response
#--------------------------------taula-reserva--------------------------------------------------#