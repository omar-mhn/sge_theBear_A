import os
from typing import List
from fastapi import FastAPI, Depends, Body, HTTPException
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
from services import read
from services.user import update_user

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users", response_model= list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user (name, email, db)
    return result

#Update user info
@app.put("/update-user/{user_id}")
def update_user_info(
    user_id: int,
    new_name: str,
    db: Session = Depends(get_db)):
    updated_user = user.update_user(user_id, new_name, db)

    return {"message": "User updated successfully", "user_id": user_id, "new_name": new_name}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user.delete_user(user_id, db)
    return {"message": "User deleted successfully"}