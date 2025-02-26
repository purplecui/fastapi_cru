from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
# URL_DATABASE = "postgresql://postgres:password@localhost:5433/blog_api"

url_database = os.getenv("URL_DATABASE")
# print(url_database)

#connection to postgres
engine = create_engine(url_database)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine) #binds session to postgres db engine

Base = declarative_base() # base class for orm