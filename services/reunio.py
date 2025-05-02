from schema.reunio_sch import reunions_schema
from sqlmodel import Session, select
from models.Reunio import Reunio

def get_all_reunions(db: Session):
    sql_read = select(Reunio)
    reunions = db.exec(sql_read).all()
    return reunions_schema(reunions)

def get_reunio(id_reunio:str, db: Session):
    sql_read = select(id_reunio).where(Reunio.id_reunio == id_reunio)
    reunio = db.exec(sql_read).one()
    return reunions_schema(reunio)

def add_new_reunio(id_reunio: str, data: str, informacio: str, nom_esdeveniment: str, db: Session):
    db_reunio = Reunio(id_reunio=id_reunio, data=data, informacio=informacio, nom_esdeveniment=nom_esdeveniment)
    db.add(db_reunio)
    db.commit()
    db.refresh(db_reunio)
    return {"Message": "Created reunion successfully"}

def update_reunio(id_reunio: str, data: str, informacio: str, nom_esdeveniment: str, db: Session):
    sql_select = select(id_reunio).where(Reunio.id_reunio == id_reunio)
    reunio_db = db.exec(sql_select).one()

    reunio_db.id_reunio = id_reunio
    reunio_db.data = data
    reunio_db.informacio = informacio
    reunio_db.nom_esdeveniment = nom_esdeveniment
    db.add(reunio_db)
    db.commit()
    return {"msg": "Updated reunion successfully"}

def delete_reunio(id_reunio: str, db: Session):
    sql_select = select(id_reunio).where(Reunio.id_reunio == id_reunio)
    reunio_db = db.exec(sql_select).one()

    db.delete(reunio_db)
    db.commit()
    return {"Msg": "Reunion deleted successfully"}
