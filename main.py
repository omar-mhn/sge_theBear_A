from typing import List
from fastapi import FastAPI
from services import read

app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result