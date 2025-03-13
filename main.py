from typing import List
from fastapi import FastAPI
from services import read

# Ampliación imports
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from detenv import load_dotenv
from services import user
import os

app = FastAPI()

@app.get(path="/root", response_model=List[dict])
async def read_root() :
    result = read.registre()
    return result

#Cargar variables de entorno
load_dotenv()

#   Configuraci´-on conexion postgresSQL
DATABASE_URL = os.getenv("DATABASE_URL") # Obtener url conexion desde .env
engine =create_engine(DATABASE_URL) #Crear engine de conexion

#Crear las tablas de la base de datos 
SQLModel.metadata.create_all(engine)

#
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model=list[dict])
def read_user(db:Session = Depends(get_db)):
    result =user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result