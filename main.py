import os
<<<<<<< HEAD
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import reunio, producte,coste
=======
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session

from services import client, comanda, planificacio, compra
>>>>>>> 29fddba1f32e2b4742836aa82c71f8348c8b115a

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
<<<<<<< HEAD
"""
#--------------------------------taula-Coste--------------------------------------------------#
@app.get("/costes/", response_model=list[dict])
async def read_costes(db: Session = Depends(get_db)):
    result = coste.get_all_costes(db)
    return result

@app.get("/costes/{id_cost}", response_model=dict)
async def read_coste_by_id(id_cost: int, db: Session = Depends(get_db)):
    result = coste.get_coste(id_cost, db)
    return result

@app.post("/costes/", response_model=dict)
async def create_coste(id_cost: int, descripcio: str, valor: float, db: Session = Depends(get_db)):
    result = coste.add_new_coste(id_cost, descripcio, valor, db)
    return result

@app.put("/update_coste/", response_model=dict)
async def update_coste(id_cost: int, descripcio: str, valor: float, db: Session = Depends(get_db)):
    result = coste.update_coste(id_cost, descripcio, valor, db)
    return result

@app.put("/update_coste_field/", response_model=dict)
async def update_coste_field(id_cost: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = coste.update_coste_field(id_cost, data, db)
    return result

@app.delete("/costes/", response_model=dict)
async def delete_coste(id_cost: int, db: Session = Depends(get_db)):
    result = coste.delete_coste(id_cost, db)
    return result
#-----------------------------final-taula-Coste------------------------------------------------#
#--------------------------------taula-Producte--------------------------------------------------#
@app.get("/productes/", response_model=list[dict])
async def read_productes(db: Session = Depends(get_db)):
    result = producte.get_all_productes(db)
    return result

@app.get("/productes/{id_producte}", response_model=dict)
async def read_producte_by_id(id_producte: int, db: Session = Depends(get_db)):
    result = producte.get_producte(id_producte, db)
    return result

@app.post("/productes/", response_model=dict)
async def create_producte(
    id_producte: int,
    cost: float,
    quantitat: int,
    nom_producte: str,
    id_proveidor: int,
    id_prestatgeria: int,
    db: Session = Depends(get_db)
):
    result = producte.add_new_producte(id_producte, cost, quantitat, nom_producte, id_proveidor, id_prestatgeria, db)
    return result

@app.put("/update_producte/", response_model=dict)
async def update_producte(
    id_producte: int,
    cost: float,
    quantitat: int,
    nom_producte: str,
    id_proveidor: int,
    id_prestatgeria: int,
    db: Session = Depends(get_db)
):
    result = producte.update_producte(id_producte, cost, quantitat, nom_producte, id_proveidor, id_prestatgeria, db)
    return result

@app.put("/update_producte_field/", response_model=dict)
async def update_producte_field(id_producte: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = producte.update_producte_field(id_producte, data, db)
    return result

@app.delete("/productes/", response_model=dict)
async def delete_producte(id_producte: int, db: Session = Depends(get_db)):
    result = producte.delete_producte(id_producte, db)
    return result
#-----------------------------final-taula-Producte------------------------------------------------#"""
#--------------------------------taula-Reunio--------------------------------------------------#
@app.get("/reunions/", response_model=list[dict])
async def read_reunions(db: Session = Depends(get_db)):
    result = reunio.get_all_reunions(db)
    return result

@app.get("/reunions/{id_reunio}", response_model=dict)
async def read_reunio_by_id(id_reunio: int, db: Session = Depends(get_db)):
    result = reunio.get_reunio(id_reunio, db)
    return result

@app.post("/reunions/", response_model=dict)
async def create_reunio(
    id_reunio: int,
    data: str,
    informacio: str,
    nom_eseveniment: str,
    db: Session = Depends(get_db)
):
    result = reunio.add_new_reunio(id_reunio, data, informacio, nom_eseveniment, db)
    return result

@app.put("/update_reunio/", response_model=dict)
async def update_reunio(
    id_reunio: int,
    data: str,
    informacio: str,
    nom_esdeveniment: str,
    db: Session = Depends(get_db)
):
    result = reunio.update_reunio(id_reunio, data, informacio, nom_esdeveniment, db)
    return result

@app.put("/update_reunio_field/", response_model=dict)
async def update_reunio_field(id_reunio: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = reunio.update_reunio_field(id_reunio, data, db)
    return result

@app.delete("/reunions/", response_model=dict)
async def delete_reunio(id_reunio: int, db: Session = Depends(get_db)):
    result = reunio.delete_reunio(id_reunio, db)
    return result
#-----------------------------final-taula-Reunio------------------------------------------------#
=======

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
#--------------------------------taula-Compra--------------------------------------------------#
@app.get("/compres/", response_model=list[dict])
async def read_compres(db: Session = Depends(get_db)):
    result = compra.get_all_compres(db)
    return result

@app.get("/compres/{id_compra}", response_model=dict)
async def read_compra_by_id(id_compra: int, db: Session = Depends(get_db)):
    result = compra.get_compra(id_compra, db)
    return result

@app.post("/compres/", response_model=dict)
async def create_compra(
    id_compra: int,
    proveïdor: str,
    productes: str,
    quantitat_producte: int,
    preu_producte: float,
    preu_total: float,
    data_compra: str,
    db: Session = Depends(get_db)
):
    result = compra.add_new_compra(
        id_compra, proveïdor, productes, quantitat_producte, preu_producte, preu_total, data_compra, db
    )
    return result

@app.put("/compres/", response_model=dict)
async def update_compra(
    id_compra: int,
    proveïdor: str,
    productes: str,
    quantitat_producte: int,
    preu_producte: float,
    preu_total: float,
    data_compra: str,
    db: Session = Depends(get_db)
):
    result = compra.update_compra(
        id_compra, proveïdor, productes, quantitat_producte, preu_producte, preu_total, data_compra, db
    )
    return result

@app.patch("/compres/", response_model=dict)
async def update_compra_field(
    id_compra: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = compra.update_compra_field(id_compra, data, db)
    return result

@app.delete("/compres/{id_compra}", response_model=dict)
async def delete_compra(id_compra: int, db: Session = Depends(get_db)):
    result = compra.delete_compra(id_compra, db)
    return result
#-----------------------------final-taula-Compra------------------------------------------------#
>>>>>>> 29fddba1f32e2b4742836aa82c71f8348c8b115a
