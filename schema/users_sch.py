def user_schema(user) -> dict:
    return {
        "user": {
            "id": user.id,  # Access attributes directly
            "name": user.name,
            "email": user.email
        }
    }

def users_schema(users: list) -> list:
    return [user_schema(user) for user in users]