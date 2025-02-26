from pydantic import BaseModel
from datetime import date


class BlogSchema(BaseModel):
    title: str
    content: str
    date:date
