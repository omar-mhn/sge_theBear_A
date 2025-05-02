import os
from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import reunio

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
