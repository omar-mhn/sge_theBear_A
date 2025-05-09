from schema.vendes_sch import vendes_schema
from sqlmodel import Session, select
from models.Venta import Venta

#--------------------------------taula-Venta---------------------------------------------------#

def get_all_vendes(db: Session):
    sql_read = select(Venta)
    vendes = db.exec(sql_read).all()
    return vendes_schema(vendes)

def get_venta(id_venta: int, db: Session):
    sql_read = select(Venta).where(Venta.id_venta == id_venta)
    venta = db.exec(sql_read).one()
    return venta.dict()

def add_new_venta(id_venta: int, cost_total: int, data_comanda: str, db: Session):
    db_venta = Venta(
        id_venta=id_venta,
        cost_total=cost_total,
        data_comanda=data_comanda
    )
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return {"Missatge": "Venta creada correctament"}

def update_venta(
    id_venta: int,
    cost_total: int,
    data_comanda: str,
    db: Session
):
    sql_select = select(Venta).where(Venta.id_venta == id_venta)
    venta_db = db.exec(sql_select).one()

    venta_db.cost_total = cost_total
    venta_db.data_comanda = data_comanda

    db.add(venta_db)
    db.commit()
    db.refresh(venta_db)
    return {"Missatge": "Venta actualitzada correctament"}

def update_venta_field(id_venta: int, data: dict, db: Session):
    sql_select = select(Venta).where(Venta.id_venta == id_venta)
    venta_db = db.exec(sql_select).one_or_none()

    if not venta_db:
        return None

    for key, value in data.items():
        if hasattr(venta_db, key) and key != "id_venta":
            setattr(venta_db, key, value)

    db.add(venta_db)
    db.commit()
    db.refresh(venta_db)
    return {"Missatge": "Camp(s) de la venta actualitzat(s) correctament"}

def delete_venta(id_venta: int, db: Session):
    sql_select = select(Venta).where(Venta.id_venta == id_venta)
    venta_db = db.exec(sql_select).one()

    db.delete(venta_db)
    db.commit()
    return {"Missatge": "Venta esborrat correctament"}

#-----------------------------final-taula-Venta------------------------------------------------#