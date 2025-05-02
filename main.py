import os
from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import reunio, producte,coste

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


@app.get("/reunions/", response_model=List[dict])
async def read_reunions(db: Session = Depends(get_db)):
    result = reunio.get_all_reunions(db)
    return result


@app.post("/reunions/", response_model=dict)
async def create_reunio(id_reunio: str, data: str, informacio: str, nom_esdeveniment: str, db: Session = Depends(get_db)):
    result = reunio.add_new_reunio(id_reunio, data, informacio, nom_esdeveniment, db)
    return result


@app.put("/update_reunio/", response_model=dict)
async def update_reunio(id_reunio: str, data: str, informacio: str, nom_esdeveniment: str, db: Session = Depends(get_db)):
    result = reunio.update_reunio(id_reunio, data, informacio, nom_esdeveniment, db)
    return result

@app.delete("/reunions/", response_model=dict)
async def delete_reunio(id_reunio: str, db: Session = Depends(get_db)):
    result = reunio.delete_reunio(id_reunio, db)
    return result

#______________Producte

@app.get("/productes/", response_model=List[dict])
async def read_productes(db: Session = Depends(get_db)):
    result = producte.get_all_productes(db)
    return result


@app.post("/productes/", response_model=dict)
async def create_producte(id_producte: str, cost: str, quantitat: str, nom_producte: str, id_proveidor: str, id_prestatgeria: str, db: Session = Depends(get_db)):
    result = producte.add_new_producte(id_producte, cost, quantitat, nom_producte, id_proveidor, id_prestatgeria, db)
    return result


@app.put("/update_producte/", response_model=dict)
async def update_producte(id_producte: str, cost: str, quantitat: str, nom_producte: str, id_proveidor: str, id_prestatgeria: str, db: Session = Depends(get_db)):
    result = producte.update_producte(id_producte, cost, quantitat, nom_producte, id_proveidor, id_prestatgeria, db)
    return result


@app.delete("/productes/", response_model=dict)
async def delete_producte(id_producte: str, db: Session = Depends(get_db)):
    result = producte.delete_producte(id_producte, db)
    return result

#----------- Coste

@app.get("/costes/", response_model=List[dict])
async def read_costes(db: Session = Depends(get_db)):
    result = coste.get_all_costes(db)
    return result


@app.post("/costes/", response_model=dict)
async def create_coste(id_factura: str, data: str, tipus_cost: str, cost_total: str, id_compra: str, id_empleat: str, id_comanda: str, db: Session = Depends(get_db)):
    result = coste.add_new_coste(id_factura, data, tipus_cost, cost_total, id_compra, id_empleat, id_comanda, db)
    return result


@app.put("/update_coste/", response_model=dict)
async def update_coste(id_factura: str, data: str, tipus_cost: str, cost_total: str, id_compra: str, id_empleat: str, id_comanda: str, db: Session = Depends(get_db)):
    result = coste.update_coste(id_factura, data, tipus_cost, cost_total, id_compra, id_empleat, id_comanda, db)
    return result


@app.delete("/costes/", response_model=dict)
async def delete_coste(id_factura: str, db: Session = Depends(get_db)):
    result = coste.delete_coste(id_factura, db)
    return result