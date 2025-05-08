#--------------------------------taula-Producte_final--------------------------------------------------#
def producte_final_schema(producte_final) -> dict:
    response = {"producte_final": producte_final}
    return response

def productes_finals_schema(productes_finals) -> list[dict]:
    response = [producte_final_schema(producte_final) for producte_final in productes_finals]
    return response
#-----------------------------final-taula-Producte_final------------------------------------------------#
