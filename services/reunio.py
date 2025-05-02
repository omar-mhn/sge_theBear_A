from schema.reunio_sch import reunions_schema
from sqlmodel import Session, select
from models.Reunio import Reunio

def get_all_reunions(db: Session):
    sql_read = select(Reunio)
    reunions = db.exec(sql_read).all()
    return reunions_schema(reunions)

def get_reunio(id_reunio: int, db: Session):
    sql_read = select(Reunio).where(Reunio.id_reunio == id_reunio)
    reunio = db.exec(sql_read).one()
    return reunions_schema([reunio])  # On retourne une liste pour rester compatible avec le schema

def add_new_reunio(id_reunio: int, data: str, informacio: str, nom_esdeveniment: str, db: Session):
    db_reunio = Reunio(
        id_reunio=id_reunio,
        data=data,
        informacio=informacio,
        nom_esdeveniment=nom_esdeveniment
    )
    db.add(db_reunio)
    db.commit()
    db.refresh(db_reunio)
    return {"Missatge": "Reunió creada correctament"}

def update_reunio(id_reunio: int, data: str, informacio: str, nom_esdeveniment: str, db: Session):
    sql_select = select(Reunio).where(Reunio.id_reunio == id_reunio)
    reunio_db = db.exec(sql_select).one()

    reunio_db.data = data
    reunio_db.informacio = informacio
    reunio_db.nom_esdeveniment = nom_esdeveniment

    db.add(reunio_db)
    db.commit()
    db.refresh(reunio_db)
    return {"Missatge": "Reunió actualitzada correctament"}

def delete_reunio(id_reunio: int, db: Session):
    sql_select = select(Reunio).where(Reunio.id_reunio == id_reunio)
    reunio_db = db.exec(sql_select).one()

    db.delete(reunio_db)
    db.commit()
    return {"Missatge": "Reunió esborrada correctament"}

def update_reunio_field(id_reunio: int, data: dict, db: Session):
    sql_select = select(Reunio).where(Reunio.id_reunio == id_reunio)
    reunio_db = db.exec(sql_select).one_or_none()

    if not reunio_db:
        return None

    for key, value in data.items():
        if hasattr(reunio_db, key) and key != "id_reunio":
            setattr(reunio_db, key, value)

    db.add(reunio_db)
    db.commit()
    db.refresh(reunio_db)
    return {"Missatge": "Camp(s) actualitzat(s) correctament"}