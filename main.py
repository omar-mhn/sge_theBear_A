from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()
SQLModel.metadata.create_all(engine)
