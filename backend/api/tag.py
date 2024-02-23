from fastapi import APIRouter
from models.models import Tag
from typing import List    
from pydantic import BaseModel

tagRouter = APIRouter()

class GetTagOutModel(BaseModel):
    id: int
    name: str

@tagRouter.get('',response_model=List[GetTagOutModel],summary="获取标签列表")
async def getTagList():
    tagList = await Tag.all()
    return tagList
