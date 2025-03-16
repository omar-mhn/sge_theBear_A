'''def schema(usr) -> dict:
    send_usr = {"id":usr["id"],
                "name":usr["name"],
                "surname":usr["surname"],
                "age":usr["age"],
                }
    return send_usr'''

'''def schemas(users) -> list[dict]:
    return [schema(user) for k,user in users.items()]'''

def user_schema(user) -> dict:
    response = {"user":user}
    return response

def users_schema(users)-> list[dict]:
    response = [user_schema(user) for user in users]
    return response
