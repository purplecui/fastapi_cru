from fastapi import FastAPI, Depends
from model import blogModel

from config.db import engine, SessionLocal
from routes.blogRoutes import blog

app = FastAPI()

app.include_router(blog)

#create all table, column in postgre
blogModel.Base.metadata.create_all(engine)

