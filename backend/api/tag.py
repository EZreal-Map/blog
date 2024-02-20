from fastapi import APIRouter
from models.models import Tag
tagRouter = APIRouter()

@tagRouter.get('',summary="获取标签列表")
async def getTagList():
    tagList = await Tag.all()
    return tagList
