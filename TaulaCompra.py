import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine, Session

from services import compra

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