from sqlalchemy import Integer, String, Column , Date
from config.db import Base

class blogModel(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    content = Column(String(255))

    date = Column(Date)
