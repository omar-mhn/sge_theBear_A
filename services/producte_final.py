from schema.productes_finals_sch import productes_finals_schema
from sqlmodel import Session, select
from models.Producte_final import Producte_final
from fastapi import HTTPException

#-----------------------------taula-Producte_final------------------------------------------------#

def get_all_productes_finals(db: Session):
    sql_read = select(Producte_final)
    productes_finals = db.exec(sql_read).all()
    return productes_finals_schema(productes_finals)

def get_producte_final(id_producto_fin: int, db: Session):
    sql_read = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final = db.exec(sql_read).one_or_none()
    if not producte_final:
        raise HTTPException(status_code=404, detail="Producte final no trobat")
    return producte_final.dict()

def add_new_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    id_comanda: int,
    db: Session
):
    db_producte_final = Producte_final(
        id_producto_fin=id_producto_fin,
        nombre=nombre,
        tipo=tipo,
        precio=precio,
        id_comanda=id_comanda
    )
    db.add(db_producte_final)
    db.commit()
    db.refresh(db_producte_final)
    return db_producte_final.dict()

def update_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    id_comanda: int,
    db: Session
):
    sql_select = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final_db = db.exec(sql_select).one_or_none()
    if not producte_final_db:
        raise HTTPException(status_code=404, detail="Producte final no trobat")

    producte_final_db.nombre = nombre
    producte_final_db.tipo = tipo
    producte_final_db.precio = precio
    producte_final_db.id_comanda = id_comanda

    db.add(producte_final_db)
    db.commit()
    db.refresh(producte_final_db)
    return producte_final_db.dict()

def update_producte_final_field(id_producto_fin: int, data: dict, db: Session):
    sql_select = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final_db = db.exec(sql_select).one_or_none()

    if not producte_final_db:
        raise HTTPException(status_code=404, detail="Producte final no trobat")

    for key, value in data.items():
        if hasattr(producte_final_db, key) and key != "id_producto_fin":
            setattr(producte_final_db, key, value)

    db.add(producte_final_db)
    db.commit()
    db.refresh(producte_final_db)
    return {"Missatge": "Camp(s) del producte final actualitzat(s) correctament"}

def delete_producte_final(id_producto_fin: int, db: Session):
    sql_select = select(Producte_final).where(Producte_final.id_producto_fin == id_producto_fin)
    producte_final_db = db.exec(sql_select).one_or_none()

    if not producte_final_db:
        raise HTTPException(status_code=404, detail="Producte final no trobat")

    db.delete(producte_final_db)
    db.commit()
    return {"Missatge": "Producte final esborrat correctament"}

#---------------------------final-taula-Producte_final----------------------------------------------#
