from schema.productes_finals_sch import productes_finals_schema
from sqlmodel import Session, select
from models.Producte_final import Producte_final

#-----------------------------taula-Producte_final------------------------------------------------#
def get_all_productes_finals(db: Session):
    sql_read = select(Producte_final)
    productes_finals = db.exec(sql_read).all()
    return productes_finals_schema(productes_finals)

def get_producte_final(id_producto_fin: int, db: Session):
    sql_read = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final = db.exec(sql_read).one()
    return producte_final.dict()

def add_new_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    comandaid: int,
    db: Session
):
    db_producte_final = Producte_final(
        id_producto_fin=id_producto_fin,
        nombre=nombre,
        tipo=tipo,
        precio=precio,
        comandaid=comandaid
    )
    db.add(db_producte_final)
    db.commit()
    db.refresh(db_producte_final)
    return {"Missatge": "Producte final creat correctament"}

def update_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    comandaid: int,
    db: Session
):
    sql_select = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final_db = db.exec(sql_select).one()

    producte_final_db.nombre = nombre
    producte_final_db.tipo = tipo
    producte_final_db.precio = precio
    producte_final_db.comandaid = comandaid

    db.add(producte_final_db)
    db.commit()
    db.refresh(producte_final_db)
    return {"Missatge": "Producte final actualitzat correctament"}

def update_producte_final_field(id_producto_fin: int, data: dict, db: Session):
    sql_select = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final_db = db.exec(sql_select).one_or_none()

    if not producte_final_db:
        return None

    for key, value in data.items():
        if hasattr(producte_final_db, key) and key != "id_producto_fin":
            setattr(producte_final_db, key, value)

    db.add(producte_final_db)
    db.commit()
    db.refresh(producte_final_db)
    return {"Missatge": "Camp(s) del producte final actualitzat(s) correctament"}

def delete_producte_final(id_producto_fin: int, db: Session):
    sql_select = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final_db = db.exec(sql_select).one()

    db.delete(producte_final_db)
    db.commit()
    return {"Missatge": "Producte final esborrat correctament"}
#---------------------------final-taula-Producte_final----------------------------------------------#