def schema(usr) -> dict:
    send_usr = {"id":usr["id"],
                "name":usr["name"],
                "surname":usr["surname"],
                "age":usr["age"],
                }
    return send_usr

def schemas(users) -> list[dict]:
    return [schema(user) for k,user in users.items()]