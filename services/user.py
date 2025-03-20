from schema.read_sch import users_schema
from sqlmodel import  Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name: str, email: str, db:Session):
    sql_read =select(User)
    users = db.exec(sql_read).all
    return users_schema(users)

def add_new_user(name: str, email: str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"mensaje":"Created user succesfully"}

def update_user(id: int, name: str, db:Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.one()
    print(user)

    user.name = name
    db.add(user)
    db.commit()
    '''db.refresh()'''

    return {"message": "update succesfully", "user":user}

def delete_user(id: int, db:Session):
    statement = select(User).where(User.id ==id)
    results = db.exec(statement)
    user = results.one()

    db.delete(user)
    db.commit()

    return {"message": "delete succesfully"}

