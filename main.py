import os
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
