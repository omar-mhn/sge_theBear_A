
def reunio_schema(reunio) -> dict:
    response = {"reunio": reunio}
    return response

def reunions_schema(reunions) -> list[dict]:
    response = [reunio_schema(reunio) for reunio in reunions]
    return response