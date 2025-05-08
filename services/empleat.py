from schema.empleats_sch import empleats_schema
from sqlmodel import Session, select
from models.Empleat import Empleat


# --------------------------------------------------MODULE-EMPLEAT--------------------------------------------------#
def get_all_empleats(db:Session):
    sql_read = select(Empleat)
    empleats = db.exec(sql_read).all()
    return empleats_schema(empleats)


def get_empleat(id_empleat: int, db: Session):
    sql_read = select(Empleat).where(Empleat.id_empleat == id_empleat)
    empleat = db.exec(sql_read).one_or_none()
    if not empleat:
        return None
    return empleat.dict()


def add_new_empleat(id_empleat:int, nom:str, email:str, telefon: str, adreca: str, rol: str, db: Session):
    db_empleat = Empleat(id_empleat=id_empleat, nom=nom, email=email, telefon=telefon, adreca=adreca, rol=rol)
    db.add(db_empleat)
    db.commit()
    db.refresh(db_empleat)
    return {"Missatge": "Empleat creat correctament"}


def update_empleat(id_empleat: int, nom: str, email: str, telefon: str, adreca: str, rol: str, db: Session):
    sql_select = select(Empleat).where(Empleat.id_empleat == id_empleat)
    empleat_db = db.exec(sql_select).one_or_none()
    if not empleat_db:
        return {"Error": "Empleat no trobat"}

    empleat_db.nom = nom
    empleat_db.email = email
    empleat_db.telefon = telefon
    empleat_db.adreca = adreca
    empleat_db.rol = rol

    db.add(empleat_db)
    db.commit()
    db.refresh(empleat_db)
    return {"Missatge": "Empleat actualitzat correctament"}


def update_empleat_field(id_empleat: int, data: dict, db: Session):
    sql_select = select(Empleat).where(Empleat.id_empleat == id_empleat)
    empleat_db = db.exec(sql_select).one_or_none()

    if not empleat_db:
        return None

    for key, value in data.items():
        if hasattr(empleat_db, key) and key != "id_empleat":
            setattr(empleat_db, key, value)

    db.add(empleat_db)
    db.commit()
    db.refresh(empleat_db)
    return {"Missatge": "Camp(s) actualitzat(s) correctament"}


def delete_empleat(id_empleat: int, db: Session):
        sql_select = select(Empleat).where(Empleat.id_empleat == id_empleat)
        empleat_db = db.exec(sql_select).one()

        db.delete(empleat_db)
        db.commit()
        return {"Missatge": "Empleat esborrat correctament"}
# --------------------------------------------------FINAL-MODULE-EMPLEAT--------------------------------------------------#