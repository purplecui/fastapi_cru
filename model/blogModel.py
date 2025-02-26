from sqlalchemy import Integer, String, Column , Date
from config.db import Base

class blogModel(Base):
    __tablename__ = "BLOGS"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), index=True)

    content = Column(String(255), index=True)

    date = Column(Date, index=True)
