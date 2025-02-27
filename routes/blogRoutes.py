from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.db import Base
from schema.blogSchema import BlogSchema
from model.blogModel import blogModel
from config.db import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

blog = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

db_dependency = Annotated[Session, Depends(get_db)]


@blog.get("/")
def read_hello():
    return {"msg":"Hello World!!"}


@blog.post("/create-blog")
async def createBlog(post: BlogSchema , db:db_dependency):
    response_data = {
        "title": post.title,
        "content": post.content,
        "date": post.date
    }
    db.add(blogModel(id=None, title=post.title, content=post.content, date=post.date))
    db.commit()
    return JSONResponse(content=jsonable_encoder(response_data), status_code=201)


@blog.get("/get-blogs")
async def getAllBlogs(
    db: db_dependency,
    page: int = Query(1, ge=1),
    limit: int= Query(5,ge=1, le=100)
):
    skip = (page -1 ) * limit
    total_count = db.query(blogModel).count()
    blogs = db.query(blogModel).offset(skip).limit(limit).all()
    return JSONResponse(content={
        "total": total_count,
        "page": page,
        "limit": limit,
        "blogs": jsonable_encoder(blogs)
        }, 
    status_code=200)

@blog.get("/get-blog/{id}")
async def getBlog(id: int, db:db_dependency):
    blog = db.query(blogModel).filter(blogModel.id == id).first()

    if blog is None:
        raise HTTPException(status_code=404, detail="blog not found")

    return JSONResponse(content=jsonable_encoder(blog), status_code=200)

@blog.put("/update-blog/{id}")
async def updateBlog(id:int, put: BlogSchema, db:db_dependency):
    blog = db.query(blogModel).filter(blogModel.id == id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail="blog not found")
    
    blog.title = put.title
    blog.content = put.content
    blog.date = put.date

    db.commit()
    db.refresh(blog)
    
    return JSONResponse(content=jsonable_encoder(blog), status_code=200)


@blog.delete("/delete-blog/{id}")
async def deleteBlog(id:int, db: db_dependency):
    blog = db.query(blogModel).filter(blogModel.id == id).first()
    
    if blog is None:
        raise HTTPException(status_code=404, detail="blog not found")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}