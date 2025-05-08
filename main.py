import os
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import empleat, participar,reserva

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

#--------------------------------MODULE-EMPLEATS--------------------------------------------------#
@app.get("/read_all_empleats/", response_model= list[dict])
async def read_empleat(db:Session = Depends(get_db)):
    result = empleat.get_all_empleats(db)
    return result

@app.get("/empleats/{id_empleat}", response_model=dict)
async def read_empleat_by_id(id_empleat: int, db: Session = Depends(get_db)):
    return empleat.get_empleat(id_empleat, db)

@app.post("/create_empleats/", response_model=dict)
async def create_empleat(id_empleat:int, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session = Depends(get_db)):
    result = empleat.add_new_empleat(id_empleat, nom, email, telefon, adreca, rol, db)
    return result

@app.put("/update_empleat/", response_model=dict)
async def update_empleat(id_empleat:int, nom: str, email:str, telefon: str, adreca: str, rol: str, db:Session = Depends(get_db)):
    result = empleat.update_empleat(id_empleat, nom, email, telefon, adreca, rol, db)
    return result

@app.patch("/empleats/{id_empleat}", response_model=dict)
async def modify_empleat_field(id_empleat: int, field: str, value: str, db: Session = Depends(get_db)):
    return empleat.update_empleat_field(id_empleat, {field: value}, db)

@app.delete("/delete_empleat/", response_model=dict)
async def delete_empleat(id_empleat:int, db:Session = Depends(get_db)):
    result = empleat.delete_empleat(id_empleat, db)
    return result

#--------------------------------FINAL-MODULE-EMPLEATS----------------------------------------------#


#-----------------------------------------TAULA-RESERVA--------------------------------------------------#
@app.get("/get_reservas/", response_model=list[dict])
async def read_reservas(db: Session = Depends(get_db)):
    return reserva.get_all_reservas(db)

@app.get("/reservas/{id_reserva}", response_model=dict)
async def read_reserva_by_id(id_reserva: int, db: Session = Depends(get_db)):
    return reserva.get_reserva(id_reserva, db)

@app.post("/create_reservas/", response_model=dict)
async def create_reserva(
    id_reserva: int, nom: str, estat: str, numPersona: int, telefon: str, data: str, id_client: int,
    db: Session = Depends(get_db)
):
    return reserva.add_new_reserva(id_reserva, nom, estat, numPersona, telefon, data, id_client, db)

@app.put("/update_reservas/{id_reserva}", response_model=dict)
async def update_reserva_details(
    id_reserva: int, nom: str, estat: str, numPersona: int, telefon: str, data: str, id_client: int,
    db: Session = Depends(get_db)
):
    return reserva.update_reserva(id_reserva, nom, estat, numPersona, telefon, data, id_client, db)

@app.patch("/update_reserva/{id_reserva}", response_model=dict)
async def modify_reserva_field(id_reserva: int, field: str, value: str, db: Session = Depends(get_db)):
    return reserva.update_reserva_field(id_reserva, {field: value}, db)

@app.delete("/delete_reservas/{id_reserva}", response_model=dict)
async def remove_reserva(id_reserva: int, db: Session = Depends(get_db)):
    return reserva.delete_reserva(id_reserva, db)

#------------------------------------final-TAULA-RESERVA--------------------------------------------------#


#---------------------------------------taula-Participar--------------------------------------------------#
@app.get("/get_participacions/", response_model=list[dict])
async def read_participacions(db: Session = Depends(get_db)):
    return participar.get_all_participacions(db)

@app.get("/participacions/{id_empleat}/{id_reunio}/{id_proveidor}", response_model=dict)
async def read_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session = Depends(get_db)):
    return participar.get_participacio(id_empleat, id_reunio, id_proveidor, db)

@app.post("/create_participacions/", response_model=dict)
async def create_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session = Depends(get_db)):
    return participar.add_new_participacio(id_empleat, id_reunio, id_proveidor, db)

@app.delete("/delete_participacions/{id_empleat}/{id_reunio}/{id_proveidor}", response_model=dict)
async def remove_participacio(id_empleat: int, id_reunio: int, id_proveidor: int, db: Session = Depends(get_db)):
    return participar.delete_participacio(id_empleat, id_reunio, id_proveidor, db)
#----------------------------------final-taula-Participar----------------------------------------------------#