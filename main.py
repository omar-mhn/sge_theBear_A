import os
from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import empleat

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

@app.get("/empleats/", response_model= list[dict])
async def read_empleat(db:Session = Depends(get_db)):
    result = empleat.get_all_empleats(db)
    return result

@app.post("/empleats/", response_model=dict)
async def create_empleat(empleatid:str, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session = Depends(get_db)):
    result = empleat.add_new_empleat(empleatid, nom, email, telefon, adreca, rol, db)
    return result


@app.put("/update_empleat/", response_model=dict)
async def update_empleat(empleatid:str, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session = Depends(get_db)):
    result = empleat.update_empleat(empleatid, nom, email, telefon, adreca, rol, db)
    return result

@app.delete("/empleats/", response_model=dict)
async def delete_empleat(empleatid:str, db:Session = Depends(get_db)):
    result = empleat.delete_empleat(empleatid, db)
    return result