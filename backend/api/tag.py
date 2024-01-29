from fastapi import APIRouter
from models.models import Tag
tagRouter = APIRouter()

@tagRouter.get('')
async def getTagList():
    tagList = await Tag.all()
    return tagList
