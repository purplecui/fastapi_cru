from fastapi import FastAPI, Depends
from model import blogModel

from config.db import engine, SessionLocal
from routes.blogRoutes import blog
import logging


#log for execution
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)




#create all table, column in postgre
blogModel.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog)


