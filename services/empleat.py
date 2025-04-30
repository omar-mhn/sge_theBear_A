from schema.empleats_sch import empleats_schema
from sqlmodel import Session, select
from models.Empleat import Empleat

def get_all_empleats(db:Session):
    sql_read = select(Empleat)
    users = db.exec(sql_read).all()
    return users_schema(empleats)

def add_new_empleat(name:str, email:str, db:Session):
    db_empleat = Empleat(name=name, email=email)
    db.add(db_empleat)
    db.commit()
    db.refresh(db_empleat)
    return {"Message":"Created empleat successfully"}