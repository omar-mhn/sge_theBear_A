import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session

from services import client, comanda, planificacio

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pots posar aquí només el teu frontend si vols més seguretat
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#--------------------------------taula-Client--------------------------------------------------#
@app.get("/clients/", response_model= list[dict])
async def read_client(db:Session = Depends(get_db)):
    result = client.get_all_clients(db)
    return result

@app.get("/clients/{id_client}", response_model=dict)
async def read_client_by_id(id_client: int, db: Session = Depends(get_db)):
    result = client.get_client(id_client, db)
    return result

@app.post("/clients/", response_model=dict)
async def create_client(id_client:int, nom: str, email:str, telefon: str, db:Session = Depends(get_db)):
    result = client.add_new_client(id_client, nom, email, telefon, db)
    return result

@app.put("/update_client/", response_model=dict)
async def update_client(id_client:int, nom: str, email:str, telefon: str, db:Session = Depends(get_db)):
    result = client.update_client(id_client, nom, email, telefon, db)
    return result

@app.put("/update_client_field/", response_model=dict)
async def update_client_field(id_client: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = client.update_client_field(id_client, data, db)
    return result

@app.delete("/clients/", response_model=dict)
async def delete_client(id_client:int, db:Session = Depends(get_db)):
    result = client.delete_client(id_client, db)
    return result
#-----------------------------final-taula-Client------------------------------------------------#
#--------------------------------taula-Comanda--------------------------------------------------#
@app.get("/comandes/", response_model=list[dict])
async def read_comandes(db: Session = Depends(get_db)):
    result = comanda.get_all_comandes(db)
    return result

@app.get("/comandes/{id_comanda}", response_model=dict)
async def read_comanda_by_id(id_comanda: int, db: Session = Depends(get_db)):
    result = comanda.get_comanda(id_comanda, db)
    return result

@app.post("/comandes/", response_model=dict)
async def create_comanda(
    id_comanda: int,
    n_taula: int,
    quantitat: int,
    producte: str,
    data: str,
    id_client: int,
    db: Session = Depends(get_db)
):
    result = comanda.add_new_comanda(
        id_comanda, n_taula, quantitat, producte, data, id_client, db
    )
    return result

@app.put("/update_comanda/", response_model=dict)
async def update_comanda(
    id_comanda: int,
    n_taula: int,
    quantitat: int,
    producte: str,
    data: str,
    id_client: int,
    db: Session = Depends(get_db)
):
    result = comanda.update_comanda(
        id_comanda, n_taula, quantitat, producte, data, id_client, db
    )
    return result

@app.put("/update_comanda_field/", response_model=dict)
async def update_comanda_field(
    id_comanda: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = comanda.update_comanda_field(id_comanda, data, db)
    return result

@app.delete("/comandes/", response_model=dict)
async def delete_comanda(id_comanda: int, db: Session = Depends(get_db)):
    result = comanda.delete_comanda(id_comanda, db)
    return result
#-----------------------------final-taula-Comanda------------------------------------------------#
#-----------------------------taula-Planificacio------------------------------------------------#
@app.get("/planificacions/", response_model=list[dict])
async def read_planificacions(db: Session = Depends(get_db)):
    result = planificacio.get_all_planificacions(db)
    return result

@app.get("/planificacions/{id_horari}", response_model=dict)
async def read_planificacio_by_id(id_horari: int, db: Session = Depends(get_db)):
    result = planificacio.get_planificacio(id_horari, db)
    return result

@app.post("/planificacions/", response_model=dict)
async def create_planificacio(
    id_horari: int,
    data: str,
    horari: int,
    rol: str,
    empleatid: int,
    db: Session = Depends(get_db)
):
    result = planificacio.add_new_planificacio(
        id_horari, data, horari, rol, empleatid, db
    )
    return result

@app.put("/update_planificacio/", response_model=dict)
async def update_planificacio(
    id_horari: int,
    data: str,
    horari: int,
    rol: str,
    empleatid: int,
    db: Session = Depends(get_db)
):
    result = planificacio.update_planificacio(
        id_horari, data, horari, rol, empleatid, db
    )
    return result

@app.put("/update_planificacio_field/", response_model=dict)
async def update_planificacio_field(
    id_horari: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = planificacio.update_planificacio_field(id_horari, data, db)
    return result

@app.delete("/planificacions/", response_model=dict)
async def delete_planificacio(id_horari: int, db: Session = Depends(get_db)):
    result = planificacio.delete_planificacio(id_horari, db)
    return result

#---------------------------final-taula-Planificacio----------------------------------------------#