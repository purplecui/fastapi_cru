from sqlalchemy import Integer, String, Column , Date
from config.db import Base

class blogPost(Base):
    __tablename__ = "BLOGS"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)

    content = Column(String, index=True)

    date = Column(Date, index=True)
