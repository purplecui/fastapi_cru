from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://postgres:password@localhost:5433/blog_api"

#connection to postgres
engine = create_engine(URL_DATABASE)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine) #binds session to postgres db engine

Base = declarative_base() # base class for orm