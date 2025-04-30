from schema.empleats_sch import empleats_schema
from sqlmodel import Session, select
from models.Empleat import Empleat

def get_all_empleats(db:Session):
    sql_read = select(Empleat)
    empleats = db.exec(sql_read).all()
    return empleats_schema(empleats)

def get_empleat(empleatid:str, db:Session):
    sql_read = select (empleatid).where(Empleat.empleatid == empleatid)
    empleat = db.exec(sql_read).one()
    return empleats_schema(empleat)

def add_new_empleat(empleatid:str, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session):
    db_empleat = Empleat(empleatid=empleatid, nom= nom, email=email, telefon=telefon, adreca=adreca, rol=rol)
    db.add(db_empleat)
    db.commit()
    db.refresh(db_empleat)
    return {"Message":"Created empleat successfully"}

def update_empleat(empleatid:str, nom: str, email:str, telefon:str, adreca:str,
                   rol:str, db:Session):
    sql_select = select(empleatid).where(Empleat.empleatid == empleatid)
    empleat_db = db.exec(sql_select).one()

    empleat_db.empleatid = empleatid
    empleat_db.nom = nom
    empleat_db.email = email
    empleat_db.telefon = telefon
    empleat_db.adreca = adreca
    empleat_db.rol = rol
    db.add(empleat_db)
    db.commit()
    return {"msg":"updated user successfully"}

def delete_empleat(empleatid:str, db:Session):
    sql_select = select(empleatid).where(Empleat.empleatid == empleatid)
    empleat_db = db.exec(sql_select).one()

    db.delete(empleat_db)
    db.commit()
    return {"Msg":"Empleat deleted successfully"}