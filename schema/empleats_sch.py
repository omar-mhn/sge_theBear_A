

def empleat_schema(empleat) -> dict:
    response = {"empleat":empleat}
    return response

def empleats_schema(empleats) -> list[dict]:
    response = [empleat_schema(empleat) for empleat in empleats]
    return response