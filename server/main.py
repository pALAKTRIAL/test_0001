from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
app = FastAPI()
SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Users/Leila/Desktop/Norbert Fenk/phase1/database/nl"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
async def root(): 
    return {"Enjoy your meal"}

@app.get("/recipt")
async def read_item(recipt_id: int, title: str = None, ingred: str = None, quantity: int = None, mesure: str = None, description: str = None):
    return {"recipt_id": recipt_id, "title": title, "ingred": ingred, "quantity": quantity, "mesure": mesure, "description": description}

@app.post("/recipt/")
async def create_item(title: str = None, ingred: str = None, quantity: int = None,  mesure: str = None, description: str = None): 
    db = SessionLocal()
    db.execute("INSERT INTO recipt (title, ingred, quantity, mesure, description) VALUES (?, ?, ?, ?, ?, ?, ?)", (title, ingred, quantity, mesure, description))
    db.commit()
    return {"title": title, "ingred": ingred, "quantity": quantity, "mesure": mesure, "description": description}

@app.delete("/recipt/{recipt_id}")
async def delete_item(recipt_id: int):
    db = SessionLocal()
    db.execute("DELETE FROM recipt WHERE id=?", (recipt_id,))
    db.commit()
    return {"deleted"}

@app.put("/recipt/{recipt_id}")
async def update_item(recipt_id: int, title: str = None, ingred: str = None, quantity: int = None, mesure: str = None, description: str = None):
    db = SessionLocal()
    db.execute("UPDATE recipt SET title=?, ingred=?, quantity=?, mesure=?, description=? WHERE id=?", (title, ingred, quantity, mesure, description, recipt_id))
    db.commit()
    return {"update"}

# data from db

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# inic templ

templates = Jinja2Templates(directory="templates")

SQLALCHEMY_DATABASE_URL = "sqlite:///C:/Users/Leila/Desktop/Norbert Fenk/phase1/database/nl"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from sqlalchemy import Column, Integer, String
class Recipe(Base):
    __tablename__ = "recipt"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    ingred = Column(String, index=True)
    quantity = Column(Integer, index=True)
    mesure = Column(String, index=True)
    description = Column(String, index=True)

Base.metadata.create_all(bind=engine)

#index.html tartalmát visszaadja
@app.get("/")
async def root(request: Request):
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    return templates.TemplateResponse("index.html", {"request": request, "recipes": recipes})

# connection db
import sqlite3
connection = sqlite3.connect("C:/Users/Leila/Desktop/Norbert Fenk/phase1/database/nl")
