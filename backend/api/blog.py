from fastapi import APIRouter
from models.models import Blog
from pydantic import BaseModel, validator
blogRouter = APIRouter()

@blogRouter.get('/list')
async def getArticle():
    blog = await Blog.all()
    return blog

@blogRouter.get('/{blog_id}')
async def getArticle(blog_id: int):
    blog = await Blog.get(id = blog_id)
    return blog


class Article(BaseModel):
    title: str
    content: str


@blogRouter.post('')
async def createArticle(blogInfo: Article):
    print(blogInfo.title, blogInfo.content)
    blog = await Blog.create(title = blogInfo.title, content = blogInfo.content)
    return {'id':blog.id}

@blogRouter.put('/{blog_id}')
async def createArticle(blog_id: int, blogInfo: Article):
    await Blog.filter(id = blog_id).update(title = blogInfo.title, content = blogInfo.content)
    return blogInfo
