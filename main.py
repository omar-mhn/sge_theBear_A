import os

from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from typing import Optional
from decimal import Decimal

from fastapi.middleware.cors import CORSMiddleware

from services import coste, empleat, client, proveidor, producte, inventari, reserva, comanda, vendre, producte_final,reunio, participar, planificacio

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

#--------------------------------taula-Coste--------------------------------------------------#
@app.get("/costes/", response_model=list[dict])
async def get_all_costes(db: Session = Depends(get_db)):
    result = coste.get_all_costes(db)
    return result

@app.get("/costes/{id_factura}", response_model=dict)
async def rget_coste(id_factura: int, db: Session = Depends(get_db)):
    result = coste.get_coste(id_factura, db)
    return result

@app.post("/create_costes/", response_model=dict)
async def add_new_coste(id_factura: int, data: str, tipus_cost: str, cost_total: int, id_compra: int, id_empleat: int, id_comanda: int,  db: Session = Depends(get_db)):
    result = coste.add_new_coste(id_factura, data, tipus_cost, cost_total, id_compra, id_empleat, id_comanda, db)
    return result

@app.put("/update_costes/", response_model=dict)
async def update_coste(id_factura: int, data: str, tipus_cost: str, cost_total: int, id_compra: int, id_empleat: int, id_comanda: int, db: Session = Depends(get_db)):
    result = coste.update_coste(id_factura, data, tipus_cost, cost_total, id_compra, id_empleat, id_comanda, db)
    return result

@app.put("/update_coste_field/", response_model=dict)
async def update_coste_field(id_factura: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = coste.update_coste_field(id_factura, data, db)
    return result

@app.delete("/delete-costes/", response_model=dict)
async def delete_coste(id_factura: int, db: Session = Depends(get_db)):
    result = coste.delete_coste(id_factura, db)
    return result
#-----------------------------final-taula-Coste------------------------------------------------#

#--------------------------------MODULE-EMPLEATS--------------------------------------------------#
@app.get("/empleats/", response_model= list[dict])
async def read_empleat(db:Session = Depends(get_db)):
    result = empleat.get_all_empleats(db)
    return result

@app.get("/empleats/{id_empleat}", response_model=dict)
async def read_empleat_by_id(id_empleat: int, db: Session = Depends(get_db)):
    return empleat.get_empleat(id_empleat, db)

@app.post("/create_empleats/", response_model=dict)
async def create_empleat(id_empleat:int, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session = Depends(get_db)):
    result = empleat.add_new_empleat(id_empleat, nom, email, telefon, adreca, rol, db)
    return result

@app.put("/update_empleats/", response_model=dict)
async def update_empleat(id_empleat:int, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session = Depends(get_db)):
    result = empleat.update_empleat(id_empleat, nom, email, telefon, adreca, rol, db)
    return result

@app.patch("/update_empleats_field/{id_empleat}", response_model=dict)
async def modify_empleat_field(id_empleat: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    return empleat.update_empleat_field(id_empleat, data, db)

@app.delete("/delete_empleats/", response_model=dict)
async def delete_empleat(id_empleat:int, db:Session = Depends(get_db)):
    result = empleat.delete_empleat(id_empleat, db)
    return result

#--------------------------------FINAL-MODULE-EMPLEATS---------------------------------------------------#

#--------------------------------taula-Client--------------------------------------------------#
@app.get("/clients/", response_model= list[dict])
async def read_client(db:Session = Depends(get_db)):
    result = client.get_all_clients(db)
    return result

@app.get("/clients/{id_client}", response_model=dict)
async def read_client_by_id(id_client: int, db: Session = Depends(get_db)):
    result = client.get_client(id_client, db)
    return result

@app.post("/create_clients/", response_model=dict)
async def create_client(id_client:int, nom: str, email:Optional[str] = None, telefon: Optional[str] = None, db:Session = Depends(get_db)):
    result = client.add_new_client(id_client, nom, email, telefon, db)
    return result

@app.put("/update_clients/", response_model=dict)
async def update_client(id_client:int, nom: str, email:Optional[str] = None, telefon: Optional[str] = None, db:Session = Depends(get_db)):
    result = client.update_client(id_client, nom, email, telefon, db)
    return result

@app.put("/update_clients_field/", response_model=dict)
async def update_client_field(id_client: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = client.update_client_field(id_client, data, db)
    return result

@app.delete("/delete_clients/", response_model=dict)
async def delete_client(id_client:int, db:Session = Depends(get_db)):
    result = client.delete_client(id_client, db)
    return result
#-----------------------------final-taula-Client------------------------------------------------#

#--------------------------------taula-Proveidor--------------------------------------------------#
@app.get("/proveidors/", response_model=list[dict])
async def read_proveidors(db: Session = Depends(get_db)):
    result = proveidor.get_all_proveidors(db)
    return result

@app.get("/proveidors/{id_proveidor}", response_model=dict)
async def read_proveidor_by_id(id_proveidor: int, db: Session = Depends(get_db)):
    result = proveidor.get_proveidor(id_proveidor, db)
    return result

@app.post("/create_proveidors/", response_model=dict)
async def create_proveidor(
    id_proveidor: int,
    nom: str,
    telefòn: str,
    email: str,
    informaciò: str,
    db: Session = Depends(get_db)
):
    result = proveidor.add_new_proveidor(
        id_proveidor, nom, telefòn, email, informaciò, db
    )
    return result

@app.put("/update_proveidors/", response_model=dict)
async def update_proveidor(
    id_proveidor: int,
    nom: str,
    telefòn: str,
    email: str,
    informaciò: str,
    db: Session = Depends(get_db)
):
    result = proveidor.update_proveidor(
        id_proveidor, nom, telefòn, email, informaciò, db
    )
    return result

@app.put("/update_proveidors_field/", response_model=dict)
async def update_proveidor_field(
    id_proveidor: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = proveidor.update_proveidor_field(id_proveidor, data, db)
    return result

@app.delete("/delete_proveidors/", response_model=dict)
async def delete_proveidor(id_proveidor: int, db: Session = Depends(get_db)):
    result = proveidor.delete_proveidor(id_proveidor, db)
    return result
#-----------------------------final-taula-Proveidor------------------------------------------------#

#--------------------------------taula-Producte--------------------------------------------------#
@app.get("/productes/", response_model=list[dict])
async def read_productes(db: Session = Depends(get_db)):
    result = producte.get_all_productes(db)
    return result

@app.get("/productes/{id_producte}", response_model=dict)
async def read_producte_by_id(id_producte: int, db: Session = Depends(get_db)):
    result = producte.get_producte(id_producte, db)
    return result

@app.post("/create_productes/create", response_model=dict)
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

@app.put("/update_productes/", response_model=dict)
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

@app.put("/update_productes_field/", response_model=dict)
async def update_producte_field(id_producte: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = producte.update_producte_field(id_producte, data, db)
    return result

@app.delete("/delete_productes/", response_model=dict)
async def delete_producte(id_producte: int, db: Session = Depends(get_db)):
    result = producte.delete_producte(id_producte, db)
    return result
#-----------------------------final-taula-Producte------------------------------------------------#

#-----------------------------taula-Inventari------------------------------------------------#
@app.get("/inventaris/", response_model=list[dict])
async def read_inventaris(db: Session = Depends(get_db)):
    result = inventari.get_all_inventaris(db)
    return result

@app.get("/inventaris/{id_estanteria}", response_model=dict)
async def read_inventari_by_id(id_estanteria: int, db: Session = Depends(get_db)):
    result = inventari.get_inventari(id_estanteria, db)
    return result

@app.post("/create_inventaris/", response_model=dict)
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

@app.put("/update_inventaris/", response_model=dict)
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

@app.put("/update_inventaris_field/", response_model=dict)
async def update_inventari_field(
    id_estanteria: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = inventari.update_inventari_field(id_estanteria, data, db)
    return result

@app.delete("/delete_inventaris/", response_model=dict)
async def delete_inventari(id_estanteria: int, db: Session = Depends(get_db)):
    result = inventari.delete_inventari(id_estanteria, db)
    return result

#-----------------------------final-taula-Inventari-----------------------------------------------#

#-----------------------------------------TAULA-RESERVA--------------------------------------------------#
@app.get("/reservas/", response_model=list[dict])
async def read_reservas(db: Session = Depends(get_db)):
    return reserva.get_all_reservas(db)

@app.get("/reservas/{id_reserva}", response_model=dict)
async def read_reserva_by_id(id_reserva: int, db: Session = Depends(get_db)):
    return reserva.get_reserva(id_reserva, db)

@app.post("/create_reservas/", response_model=dict)
async def create_reserva(
    id_reserva: int, nom: str, estat: str, numPersona: int, telefon: str, data: str, id_client: int,
    db: Session = Depends(get_db)
):
    return reserva.add_new_reserva(id_reserva, nom, estat, numPersona, telefon, data, id_client, db)

@app.put("/update_reservas/{id_reserva}", response_model=dict)
async def update_reserva_details(
    id_reserva: int, nom: str, estat: str, numPersona: int, telefon: str, data: str, id_client: int,
    db: Session = Depends(get_db)
):
    return reserva.update_reserva(id_reserva, nom, estat, numPersona, telefon, data, id_client, db)

@app.patch("/update_reservas_field/{id_reserva}", response_model=dict)
async def modify_reserva_field(id_reserva: int, field: str, value: str, db: Session = Depends(get_db)):
    return reserva.update_reserva_field(id_reserva, {field: value}, db)

@app.delete("/delete_reservas/{id_reserva}", response_model=dict)
async def remove_reserva(id_reserva: int, db: Session = Depends(get_db)):
    return reserva.delete_reserva(id_reserva, db)

#------------------------------------final-TAULA-RESERVA--------------------------------------------------#

#--------------------------------taula-Comanda--------------------------------------------------#
@app.get("/comandes/", response_model=list[dict])
async def read_comandes(db: Session = Depends(get_db)):
    result = comanda.get_all_comandes(db)
    return result

@app.get("/comandes/{id_comanda}", response_model=dict)
async def read_comanda_by_id(id_comanda: int, db: Session = Depends(get_db)):
    result = comanda.get_comanda(id_comanda, db)
    return result

@app.post("/create_comandes/", response_model=dict)
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

@app.put("/update_comandes/", response_model=dict)
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

@app.put("/update_comandes_field/", response_model=dict)
async def update_comanda_field(
    id_comanda: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = comanda.update_comanda_field(id_comanda, data, db)
    return result

@app.delete("/delete_comandes/", response_model=dict)
async def delete_comanda(id_comanda: int, db: Session = Depends(get_db)):
    result = comanda.delete_comanda(id_comanda, db)
    return result
#-----------------------------final-taula-Comanda------------------------------------------------#

#--------------------------------taula-Vendre--------------------------------------------------#
@app.get("/compres/", response_model=list[dict])
async def read_vendes(db: Session = Depends(get_db)):
    result = vendre.get_all_compres(db)
    return result

@app.get("/compres/{id_compra}", response_model=dict)
async def read_venta_by_id(id_compra: int, db: Session = Depends(get_db)):
    result = vendre.get_compres(id_compra, db)
    return result

@app.post("/create_compres/", response_model=dict)
async def create_venta(
    id_compra: int,
    cost_total: Decimal,
    data_comanda: str,
    db: Session = Depends(get_db)
):
    result = vendre.add_create_compres(
        id_compra, cost_total, data_comanda, db
    )
    return result

@app.put("/update_compres/", response_model=dict)
async def update_venta(
    id_compra: int,
    cost_total: Decimal,
    data_comanda: str,
    db: Session = Depends(get_db)
):
    result = vendre.update_compres(
        id_compra, cost_total, data_comanda, db
    )
    return result

@app.put("/update_compres_field/", response_model=dict)
async def update_venta_field(
    id_compra: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = vendre.update_compres_field(id_compra, data, db)
    return result

@app.delete("/delete_compres/", response_model=dict)
async def delete_venta(id_compra: int, db: Session = Depends(get_db)):
    result = vendre.delete_compres(id_compra, db)
    return result
#-----------------------------final-taula-Venta------------------------------------------------#

#-----------------------------taula-Producte_final------------------------------------------------#
@app.get("/productes_finals/", response_model=list[dict])
async def read_productes_finals(db: Session = Depends(get_db)):
    result = producte_final.get_all_productes_finals(db)
    return result

@app.get("/productes_finals/{id_producto_fin}", response_model=dict)
async def read_producte_final_by_id(id_producto_fin: int, db: Session = Depends(get_db)):
    result = producte_final.get_producte_final(id_producto_fin, db)
    return result

@app.post("/create_productes_finals/", response_model=dict)
async def create_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    id_comanda: int,
    db: Session = Depends(get_db)
):
    result = producte_final.add_new_producte_final(
        id_producto_fin, nombre, tipo, precio, id_comanda, db
    )
    return result

@app.put("/update_productes_final/", response_model=dict)
async def update_producte_final(
    id_producto_fin: int,
    nombre: str,
    tipo: str,
    precio: float,
    id_comanda: int,
    db: Session = Depends(get_db)
):
    result = producte_final.update_producte_final(
        id_producto_fin, nombre, tipo, precio, id_comanda, db
    )
    return result

@app.put("/update_productes_final_field/", response_model=dict)
async def update_producte_final_field(
    id_producto_fin: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = producte_final.update_producte_final_field(id_producto_fin, data, db)
    return result

@app.delete("/delete_productes_finals/", response_model=dict)
async def delete_producte_final(id_producto_fin: int, db: Session = Depends(get_db)):
    result = producte_final.delete_producte_final(id_producto_fin, db)
    return result
#-----------------------------final-taula-Producte_final------------------------------#

#--------------------------------taula-Reunio--------------------------------------------------#
@app.get("/reunions/", response_model=list[dict])
async def read_reunions(db: Session = Depends(get_db)):
    result = reunio.get_all_reunions(db)
    return result

@app.get("/reunions/{id_reunio}", response_model=dict)
async def get_reunio(id_reunio: int, db: Session = Depends(get_db)):
    result = reunio.get_reunio(id_reunio, db)
    return result

@app.post("/create_reunions/", response_model=dict)
async def create_reunio(
    id_reunio: int,
    data: str,
    informacio: str,
    nom_eseveniment: str,
    db: Session = Depends(get_db)
):
    result = reunio.add_new_reunio(id_reunio, data, informacio, nom_eseveniment, db)
    return result

@app.put("/update_reunions/", response_model=dict)
async def update_reunio(
    id_reunio: int,
    data: str,
    informacio: str,
    nom_esdeveniment: str,
    db: Session = Depends(get_db)
):
    result = reunio.update_reunio(id_reunio, data, informacio, nom_esdeveniment, db)
    return result

@app.put("/update_reunions_field/", response_model=dict)
async def update_reunio_field(id_reunio: int, field: str, value: str, db: Session = Depends(get_db)):
    data = {field: value}
    result = reunio.update_reunio_field(id_reunio, data, db)
    return result

@app.delete("/delete_reunions/", response_model=dict)
async def delete_reunio(id_reunio: int, db: Session = Depends(get_db)):
    result = reunio.delete_reunio(id_reunio, db)
    return result
#-----------------------------final-taula-Reunio------------------------------------------------#

#---------------------------------------taula-Participar--------------------------------------------------#
@app.get("/participacions/", response_model=list[dict])
async def read_participacions(db: Session = Depends(get_db)):
    return participar.get_all_participacions(db)

@app.get("/participacions/{id_empleat}/{id_reunio}/{id_proveidor}", response_model=dict)
async def read_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session = Depends(get_db)):
    return participar.get_participacio(id_empleat, id_reunio, id_proveidor, db)

@app.post("/create_participacions/", response_model=dict)
async def create_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session = Depends(get_db)):
    return participar.add_new_participacio(id_empleat, id_reunio, id_proveidor, db)

@app.delete("/delete_participacions/{id_empleat}/{id_reunio}/{id_proveidor}", response_model=dict)
async def remove_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session = Depends(get_db)):
    return participar.delete_participacio(id_empleat, id_reunio, id_proveidor, db)
#----------------------------------final-taula-Participar----------------------------------------------------#

#-----------------------------taula-Planificacio------------------------------------------------#
@app.get("/planificacions/", response_model=list[dict])
async def get_all_planificacions(db: Session = Depends(get_db)):
    result = planificacio.get_all_planificacions(db)
    return result

@app.get("/planificacions/{id_horari}", response_model=dict)
async def get_planificacio(id_horari: int, db: Session = Depends(get_db)):
    result = planificacio.get_planificacio(id_horari, db)
    return result

@app.post("/create_planificacions/", response_model=dict)
async def add_new_planificacio(
    id_horari: int,
    data: str,
    horari: str,
    rol: str,
    id_empleat: int,
    db: Session = Depends(get_db)
):
    result = planificacio.add_new_planificacio(
        id_horari, data, horari, rol, id_empleat, db
    )
    return result

@app.put("/update_planificacions/", response_model=dict)
async def update_planificacio(
    id_horari: int,
    data: str,
    horari: str,
    rol: str,
    id_empleat: int,
    db: Session = Depends(get_db)
):
    result = planificacio.update_planificacio(
        id_horari, data, horari, rol, id_empleat, db
    )
    return result

@app.put("/update_planificacions_field/", response_model=dict)
async def update_planificacio_field(
    id_horari: int,
    field: str,
    value: str,
    db: Session = Depends(get_db)
):
    data = {field: value}
    result = planificacio.update_planificacio_field(id_horari, data, db)
    return result

@app.delete("/delete_planificacions/", response_model=dict)
async def delete_planificacio(id_horari: int, db: Session = Depends(get_db)):
    result = planificacio.delete_planificacio(id_horari, db)
    return result

#---------------------------final-taula-Planificacio----------------------------------------------#