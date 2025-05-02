from schema.clients_sch import clients_schema
from sqlmodel import Session, select
from models.Client import Client

def get_all_clients(db:Session):
    sql_read = select(Client)
    clients = db.exec(sql_read).all()
    return clients_schema(clients)

def get_client(id_client:int, db:Session):
    sql_read = select(Client).where(Client.id_client == id_client)
    client = db.exec(sql_read).one()
    return client.dict()

def add_new_client(id_client:int, nom: str, email:str, telefon: str, db:Session):
    db_client = Client(id_client=id_client, nom= nom, email=email, telefon=telefon)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"Message":"Created client successfully"}

def update_client(id_client:int, nom: str, email:str, telefon:str, db:Session):
    sql_select = select(Client).where(Client.id_client == id_client)
    client_db = db.exec(sql_select).one()

    client_db.id_client = id_client
    client_db.nom = nom
    client_db.email = email
    client_db.telefon = telefon
    db.add(client_db)
    db.commit()
    db.refresh(client_db)
    return {"msg":"Client actualitzat correctament"}

def update_client_field(id_client: int, data: dict, db: Session):
    sql_select = select(Client).where(Client.id_client == id_client)
    client_db = db.exec(sql_select).one_or_none()

    if not client_db:
        return None

    for key, value in data.items():
        if hasattr(client_db, key) and key != "id_client":
            setattr(client_db, key, value)

    db.add(client_db)
    db.commit()
    db.refresh(client_db)
    return {"msg": f"Camp(s) actualitzat(s) correctament"}

def delete_client(id_client:int, db:Session):
    sql_select = select(Client).where(Client.id_client == id_client)
    client_db = db.exec(sql_select).one()

    db.delete(client_db)
    db.commit()
    return {"Msg":"Empleat deleted successfully"}