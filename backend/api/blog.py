from fastapi import APIRouter, Query
from models.models import Blog,Tag
from pydantic import BaseModel, validator
blogRouter = APIRouter()


@blogRouter.get('',summary="获取文章列表",description="获取文章列表，支持分页和标签过滤")
async def getArticle(limit: int = Query(None, description="Limit the number of articles", ge=1), tag: str = Query(None, description="Filter articles by tag")):
    if limit:
        blog_limit = await Blog.all().order_by('-created_at').limit(limit)
        return blog_limit
    if tag:
        # 使用 prefetch_related 优化查询
        blog_tag = await Blog.filter(tag__name=tag).prefetch_related('tag').order_by('-created_at')
        return blog_tag
    blog_all = await Blog.all().order_by('-created_at')
    return blog_all

@blogRouter.get('/{blog_id}',summary="获取文章详情",description="获取文章详情")
async def getArticle(blog_id: int):
    blog = await Blog.get(id = blog_id)
    return blog


class ArticleValidator(BaseModel):
    title: str
    content: str
    tag: str


@blogRouter.post('',summary="创建文章",description="创建文章")
async def createArticle(blogInfo: ArticleValidator):
    # 尝试从 Tag 表中获取对应的 tag 记录，如果不存在，则创建新的 Tag 记录
    [tag_instance, _] = await Tag.get_or_create(name=blogInfo.tag)
    # 第二个参数是 IsNewTag 的布尔值，如果为 True，则表示新创建了一个 Tag 记录，
    # 否则表示从数据库中获取了一个已存在的 Tag 记录。
    
    # 创建新的 Blog 记录，并关联到对应的 Tag，foreign_key要传入实例对象tag，不仅仅tag.id
    blog = await Blog.create(title=blogInfo.title, content=blogInfo.content, tag=tag_instance)
    
    return blog

@blogRouter.put('/{blog_id}',summary="更新文章",description="更新文章")
async def createArticle(blog_id: int, blogInfo: ArticleValidator):
    # 获取或创建标签
    tag_instance, _ = await Tag.get_or_create(name=blogInfo.tag)
    # 更新文章
    await Blog.filter(id = blog_id).update(title = blogInfo.title, content = blogInfo.content, tag=tag_instance)
     # 返回更新后的博客信息
    updated_blog = await Blog.get(id=blog_id)
    return updated_blog
