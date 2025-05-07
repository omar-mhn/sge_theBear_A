#--------------------------------taula-Cost--------------------------------------------------#
def cost_schema(cost) -> dict:
    response = {"cost": cost}
    return response

def costs_schema(costs) -> list[dict]:
    response = [cost_schema(cost) for cost in costs]
    return response

#-----------------------------final-taula-Cost------------------------------------------------#