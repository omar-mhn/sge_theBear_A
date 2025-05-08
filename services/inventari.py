from schema.inventaris_sch import inventaris_schema
from sqlmodel import Session, select
from models.Inventari import Inventari

#-----------------------------taula-Inventari------------------------------------------------#
def get_all_inventaris(db: Session):
    sql_read = select(Inventari)
    inventaris = db.exec(sql_read).all()
    return inventaris_schema(inventaris)

def get_inventari(id_estanteria: int, db: Session):
    sql_read = select(Inventari).where(Inventari.id_estanteria == id_estanteria)
    inventari = db.exec(sql_read).one()
    return inventari.dict()

def add_new_inventari(
    id_estanteria: int,
    nombre_materia_prima: str,
    cantidad_min: int,
    fecha_entrada: str,
    fecha_caducidad: str,
    stock: int,
    db: Session
):
    db_inventari = Inventari(
        id_estanteria=id_estanteria,
        nombre_materia_prima=nombre_materia_prima,
        cantidad_min=cantidad_min,
        fecha_entrada=fecha_entrada,
        fecha_caducidad=fecha_caducidad,
        stock=stock
    )
    db.add(db_inventari)
    db.commit()
    db.refresh(db_inventari)
    return {"Missatge": "Inventari creat correctament"}

def update_inventari(
    id_estanteria: int,
    nombre_materia_prima: str,
    cantidad_min: int,
    fecha_entrada: str,
    fecha_caducidad: str,
    stock: int,
    db: Session
):
    sql_select = select(Inventari).where(Inventari.id_estanteria == id_estanteria)
    inventari_db = db.exec(sql_select).one()

    inventari_db.nombre_materia_prima = nombre_materia_prima
    inventari_db.cantidad_min = cantidad_min
    inventari_db.fecha_entrada = fecha_entrada
    inventari_db.fecha_caducidad = fecha_caducidad
    inventari_db.stock = stock

    db.add(inventari_db)
    db.commit()
    db.refresh(inventari_db)
    return {"Missatge": "Inventari actualitzat correctament"}

def update_inventari_field(id_estanteria: int, data: dict, db: Session):
    sql_select = select(Inventari).where(Inventari.id_estanteria == id_estanteria)
    inventari_db = db.exec(sql_select).one_or_none()

    if not inventari_db:
        return None

    for key, value in data.items():
        if hasattr(inventari_db, key) and key != "id_estanteria":
            setattr(inventari_db, key, value)

    db.add(inventari_db)
    db.commit()
    db.refresh(inventari_db)
    return {"Missatge": "Camp(s) de l'inventari actualitzat(s) correctament"}

def delete_inventari(id_estanteria: int, db: Session):
    sql_select = select(Inventari).where(Inventari.id_estanteria == id_estanteria)
    inventari_db = db.exec(sql_select).one()

    db.delete(inventari_db)
    db.commit()
    return {"Missatge": "Inventari esborrat correctament"}
#---------------------------final-taula-Inventari----------------------------------------------#