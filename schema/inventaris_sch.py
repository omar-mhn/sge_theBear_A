#--------------------------------taula-Inventari--------------------------------------------------#
def inventari_schema(inventari) -> dict:
    response = {"inventari": inventari}
    return response

def inventaris_schema(inventaris) -> list[dict]:
    response = [inventari_schema(inventari) for inventari in inventaris]
    return response

#-----------------------------final-taula-Inventari------------------------------------------------#