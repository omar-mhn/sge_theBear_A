import os
from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import client
from fastapi.middleware.cors import CORSMiddleware

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