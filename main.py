from typing import List
from fastapi import FastAPI, Depends
from services import read,user
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
DATABASE_URL = os.getenv("DATABASE_URL") # Obtenir la URL de connexió de .env
engine = create_engine(DATABASE_URL)  # Crear l'engine de connexió

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
    result = user.get_all_users(db)
    return result

#6. añadir usuarios
@app.post("/users/", response_model=dict)
def create_user(name: str,email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users/", response_model=dict)
async def update_user(id: int, name: str, db: Session = Depends(get_db)):
    result = user.update_user(id, name, db)
    return result

@app.delete("/users/", response_model=dict)
async def delete_user(id: int, db: Session = Depends(get_db)):
    result = user.delete_user(id, db)
    return result