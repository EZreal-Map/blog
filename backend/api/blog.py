from fastapi import APIRouter
from models.models import Blog
from pydantic import BaseModel, validator
blog = APIRouter()

@blog.get('/list')
async def getArticle():
    blog = await Blog.all()
    return blog

@blog.get('/{blog_id}')
async def getArticle(blog_id: int):
    blog = await Blog.get(id = blog_id)
    return blog


class Article(BaseModel):
    title: str
    content: str


@blog.post('')
async def createArticle(blog: Article):
    blog = await Blog.create(title = blog.title, content = blog.content)
    return blog

@blog.put('/{blog_id}')
async def createArticle(blog_id: int, blog: Article):
    await Blog.filter(id = blog_id).update(title = blog.title, content = blog.content)
    return blog
