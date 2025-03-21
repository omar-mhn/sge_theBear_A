from sqlmodel.sql._expression_select_cls import SelectBase

from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name: str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message":"Created user successfully"}

def update_user(id: int, name: str, db:Session):
    query = select(User).where(User.id == id)
    result = db.exec(query)
    user = result.one()
    print(user)

    user.name = name
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "update succesfully", "user":user}

def delete_user(id: int, db:Session):
    query = select(User).where(User.id == id)
    result = db.exec(query)
    user = result.one()
    db.delete(user)