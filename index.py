from fastapi import FastAPI, Depends
from model import blogModel
from typing import Annotated
from pydantic import BaseModel
from config.db import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import date

app = FastAPI()

#create all table, column in postgre
blogModel.Base.metadata.create_all(engine)


#schema
class BlogPostSchema(BaseModel):
    title: str
    content: str
    date:date

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  


db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_hello():
    return {"msg":"Hello World!!"}

