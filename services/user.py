from schema.read_sch import users_schema
from sqlmodel import  Session, select
from models.User import User

def update_user(id: int, db:Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement).all
    user = results.one()
    print(user)

