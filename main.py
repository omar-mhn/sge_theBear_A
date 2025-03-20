from typing import List
from fastapi import FastAPI
from services import read

# Ampliación imports
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os

app = FastAPI()

@app.get(path="/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

# Cargar variables de entorno
load_dotenv()

# Configuración conexión PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")  # Obtener URL conexión desde .env
engine = create_engine(DATABASE_URL)  # Crear engine de conexión

# Crear las tablas de la base de datos
SQLModel.metadata.create_all(engine)

# Gestiona la sesión de la base de datos
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

#Obtiene todos los usuarios 
@app.get("/users/", response_model=list[dict])
def read_user(db:Session = Depends(get_db)):
    result =user.get_all_users(db)
    return result

#Crea nuevo usuario 
@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

# Actualiza el nombre de un usuario existente
@app.put("/users/{user_id}", response_model=dict)
def update_user(user_id: int, name: str, db: Session = Depends(get_db)):
    result = user.update_one_user(user_id, name, db)
    return result

# Elimina un usuario
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    result = user.delete_one_user(user_id, db)
    return result
