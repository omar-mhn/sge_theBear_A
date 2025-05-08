#--------------------------------taula-Venta--------------------------------------------------#
def venta_schema(venta) -> dict:
    response = {"venta": venta}
    return response

def vendes_schema(vendes) -> list[dict]:
    response = [venta_schema(vendes) for vendes in vendes]
    return response

#-----------------------------final-taula-Venta------------------------------------------------#