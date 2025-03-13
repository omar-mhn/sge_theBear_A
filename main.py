from typing import List
from fastapi import FastAPI, Depends
from services import read
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

app = FastAPI()

"""@app.get("/root",response_model = List[dict])
async def read_root():
    result = read.registre()
    return result"""

#1. Carregar variables d'entorn
load_dotenv()

#2. Configurar la connexio a postgreSQL
DATABAASE_URL = os.getenv("DATABASE_URL") # Obtenir la URL de connexió de .env
engine = create_engine(DATABAASE_URL)  # Crear l'engine de connexió

#3. Crear les taules a la base de dades
SQLModel.metadata.create_all(engine)

#4. como cursor
def get_db():
    db= Session(engine)
    try:
        yield  db
    finally:
        db.close()

#5.
@app.get("/users/", response_model=list[dict])
def read_user(db:Session = Depends(get_db)):
    result = read.get_all_users(db)
    return result

#6. añadir usuarios
@app.post("/users/", response_model=dict)
def create_user(name: str,email:str, db:Session = Depends(get_db)):
    result = read.add_new_user(name, email, db)
    return result


