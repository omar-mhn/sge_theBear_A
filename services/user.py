from schema.users_sch import users_schema
from sqlmodel import Session, select 
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name:str, email:str, db:Session):
    sql_read =select(User)
    users = db.exec(sql_read).all
    return users_schema(users)

def add_new_user(name: str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Usuario creado correctamente"} #DICCIONARIO CORRECTO 

# PROPUESTA endpoint para actualizar solo el nombre del usuario por id
def update_one_user(user_id: int, name: str, db: Session):
    statement = select(User).where(User.id == user_id)
    results = db.exec(statement)
    user = results.one_or_none()

    if not user:
        return {"error": "Usuario no encontrado"}

    user.name = name  # Solo se permite actualizar el nombre
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "Usuario actualizado correctamente", "user": user}

# PROPUESTA endpoint para eliminar usuario por ID
def delete_one_user(user_id: int, db: Session):
    statement = select(User).where(User.id == user_id)
    results = db.exec(statement)
    user = results.one_or_none()

    if not user:
        return {"error": "Usuario no encontrado"}

    db.delete(user)
    db.commit()

    return {"message": "Usuario eliminado correctamente"}
