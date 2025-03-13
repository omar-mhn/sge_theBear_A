def user_schema(user) -> dict:
    response = {"user":user}
    return response

def users_schema(users)-> list[dict]:
    response =[user_schema(user) for user in users]
    return response