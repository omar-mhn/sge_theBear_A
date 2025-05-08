from schema.reservas_sch import reservas_schema
from sqlmodel import Session, select
from models.Reserva import Reserva

#--------------------------------TAULA-RESERVA---------------------------------------------------#
def get_all_reservas(db: Session):
    sql_read = select(Reserva)
    reservas = db.exec(sql_read).all()
    return reservas_schema(reservas)

def get_reserva(id_reserva: int, db: Session):
    sql_read = select(Reserva).where(Reserva.id_reserva == id_reserva)
    reserva = db.exec(sql_read).one()
    return reserva.dict()

def add_new_reserva(id_reserva: int, nom: str, estat: str, numPersona: int, telefon: str, data: str, id_client: int, db: Session):
    db_reserva = Reserva(
        id_reserva=id_reserva,
        nom=nom,
        estat=estat,
        numPersona=numPersona,
        telefon=telefon,
        data=data,
        id_client=id_client
    )
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return {"Missatge": "Reserva creada correctament"}

def update_reserva(
    id_reserva: int,
    nom: str,
    estat: str,
    numPersona: int,
    telefon: str,
    data: str,
    id_client: int,
    db: Session
):
    sql_select = select(Reserva).where(Reserva.id_reserva == id_reserva)
    reserva_db = db.exec(sql_select).one()

    reserva_db.nom = nom
    reserva_db.estat = estat
    reserva_db.numPersona = numPersona
    reserva_db.telefon = telefon
    reserva_db.data = data
    reserva_db.id_client = id_client

    db.add(reserva_db)
    db.commit()
    db.refresh(reserva_db)
    return {"Missatge": "Reserva actualitzada correctament"}

def update_reserva_field(id_reserva: int, data: dict, db: Session):
    sql_select = select(Reserva).where(Reserva.id_reserva == id_reserva)
    reserva_db = db.exec(sql_select).one_or_none()

    if not reserva_db:
        return None

    for key, value in data.items():
        if hasattr(reserva_db, key) and key != "id_reserva":
            setattr(reserva_db, key, value)

    db.add(reserva_db)
    db.commit()
    db.refresh(reserva_db)
    return {"Missatge": "Camp(s) de la reserva actualitzat(s) correctament"}

def delete_reserva(id_reserva: int, db: Session):
    sql_select = select(Reserva).where(Reserva.id_reserva == id_reserva)
    reserva_db = db.exec(sql_select).one()

    db.delete(reserva_db)
    db.commit()
    return {"Missatge": "Reserva esborrada correctament"}
#-----------------------------final-TAULA-RESERVA------------------------------------------------#