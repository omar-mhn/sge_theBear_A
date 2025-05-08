import os

from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import inventari, producte_final, reunio, producte,coste

from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session

from services import client, comanda, planificacio, proveïdor, venta

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
#-----------------------------final-taula-Producte------------------------------------------------#
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

#--------------------------------taula-Proveïdor--------------------------------------------------#
@app.get("/proveïdors/", response_model=list[dict])
async def read_proveïdors(db: Session = Depends(get_db)):
    result = proveïdor.get_all_proveïdors(db)
    return result

@app.get("/proveïdors/{id_proveïdor}", response_model=dict)
async def read_proveïdor_by_id(id_proveïdor: int, db: Session = Depends(get_db)):
    result = proveïdor.get_proveïdor(id_proveïdor, db)
    return result

@app.post("/proveïdors/", response_model=dict)
async def create_proveïdor(
    id_proveïdor: int,
    nom: str,
    telefòn: str,
    email: str,
    informaciò: str,
    db: Session = Depends(get_db)
):
    result = proveïdor.add_new_proveïdor(
        id_proveïdor, nom, telefòn, email, informaciò, db
    )
    return result

@app.put("/update_proveïdor/", response_model=dict)
async def update_proveïdor(
    id_proveïdor: int,
    nom: str,
    telefòn: str,
    email: str,
    informaciò: str,
    db: Session = Depends(get_db)
):
    result = proveïdor.update_proveïdor(
        id_proveïdor, nom, telefòn, email, informaciò, db
    )
    return result

@app.put("/update_proveïdor_field/", response_model=dict)
async def update_proveïdor_field(
    id_proveïdor: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = proveïdor.update_proveïdor_field(id_proveïdor, data, db)
    return result

@app.delete("/proveïdors/", response_model=dict)
async def delete_proveïdor(id_proveïdor: int, db: Session = Depends(get_db)):
    result = proveïdor.delete_proveïdor(id_proveïdor, db)
    return result
#-----------------------------final-taula-Proveïdor------------------------------------------------#

#--------------------------------taula-Venta--------------------------------------------------#
@app.get("/vendes/", response_model=list[dict])
async def read_vendes(db: Session = Depends(get_db)):
    result = venta.get_all_vendes(db)
    return result

@app.get("/vendes/{id_venta}", response_model=dict)
async def read_venta_by_id(id_venta: int, db: Session = Depends(get_db)):
    result = venta.get_venta(id_venta, db)
    return result

@app.post("/vendes/", response_model=dict)
async def create_venta(
    id_venta: int,
    cost_total: int,
    data_comanda: str,
    db: Session = Depends(get_db)
):
    result = venta.add_new_venta(
        id_venta, cost_total, data_comanda, db
    )
    return result

@app.put("/update_venta/", response_model=dict)
async def update_venta(
    id_venta: int,
    cost_total: int,
    data_comanda: str,
    db: Session = Depends(get_db)
):
    result = venta.update_venta(
        id_venta, cost_total, data_comanda, db
    )
    return result

@app.put("/update_venta_field/", response_model=dict)
async def update_venta_field(
    id_venta: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = venta.update_venta_field(id_venta, data, db)
    return result

@app.delete("/vendes/", response_model=dict)
async def delete_venta(id_venta: int, db: Session = Depends(get_db)):
    result = venta.delete_venta(id_venta, db)
    return result
#-----------------------------final-taula-Venta------------------------------------------------#

#-----------------------------taula-Inventari------------------------------------------------#
@app.get("/inventaris/", response_model=list[dict])
async def read_inventaris(db: Session = Depends(get_db)):
    result = inventari.get_all_inventaris(db)
    return result

@app.get("/inventaris/{id_estanteria}", response_model=dict)
async def read_inventari_by_id(id_estanteria: int, db: Session = Depends(get_db)):
    result = inventari.get_inventari(id_estanteria, db)
    return result

@app.post("/inventaris/", response_model=dict)
async def create_inventari(
    id_estanteria: int,
    nombre_materia_prima: str,
    cantidad_min: int,
    fecha_entrada: str,
    fecha_caducidad: str,
    stock: int,
    db: Session = Depends(get_db)
):
    result = inventari.add_new_inventari(
        id_estanteria, nombre_materia_prima, cantidad_min, fecha_entrada, fecha_caducidad, stock, db
    )
    return result

@app.put("/update_inventari/", response_model=dict)
async def update_inventari(
    id_estanteria: int,
    nombre_materia_prima: str,
    cantidad_min: int,
    fecha_entrada: str,
    fecha_caducidad: str,
    stock: int,
    db: Session = Depends(get_db)
):
    result = inventari.update_inventari(
        id_estanteria, nombre_materia_prima, cantidad_min, fecha_entrada, fecha_caducidad, stock, db
    )
    return result

@app.put("/update_inventari_field/", response_model=dict)
async def update_inventari_field(
    id_estanteria: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = inventari.update_inventari_field(id_estanteria, data, db)
    return result

@app.delete("/inventaris/", response_model=dict)
async def delete_inventari(id_estanteria: int, db: Session = Depends(get_db)):
    result = inventari.delete_inventari(id_estanteria, db)
    return result

#-----------------------------final-taula-Inventari-----------------------------------------------#
#-----------------------------taula-Producte_final------------------------------------------------#
@app.get("/productes_finals/", response_model=list[dict])
async def read_productes_finals(db: Session = Depends(get_db)):
    result = producte_final.get_all_productes_finals(db)
    return result

@app.get("/productes_finals/{id_producto_fin}", response_model=dict)
async def read_producte_final_by_id(id_producto_fin: int, db: Session = Depends(get_db)):
    result = producte_final.get_producte_final(id_producto_fin, db)
    return result

@app.post("/productes_finals/", response_model=dict)
async def create_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    comandaid: int,
    db: Session = Depends(get_db)
):
    result = producte_final.add_new_producte_final(
        id_producto_fin, nombre, tipo, precio, comandaid, db
    )
    return result

@app.put("/update_producte_final/", response_model=dict)
async def update_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    comandaid: int,
    db: Session = Depends(get_db)
):
    result = producte_final.update_producte_final(
        id_producto_fin, nombre, tipo, precio, comandaid, db
    )
    return result

@app.put("/update_producte_final_field/", response_model=dict)
async def update_producte_final_field(
    id_producto_fin: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = producte_final.update_producte_final_field(id_producto_fin, data, db)
    return result

@app.delete("/productes_finals/", response_model=dict)
async def delete_producte_final(id_producto_fin: int, db: Session = Depends(get_db)):
    result = producte_final.delete_producte_final(id_producto_fin, db)
    return result
#-----------------------------final-taula-Producte_final------------------------------------------------#
