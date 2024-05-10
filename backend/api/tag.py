from fastapi import APIRouter, Depends
from models.models import Tag
from typing import List    
from pydantic import BaseModel
from core.Authenticate import is_admin_user

tagRouter = APIRouter()

class GetTagOutModel(BaseModel):
    id: int
    name: str

@tagRouter.get('',response_model=List[GetTagOutModel],summary="获取标签列表")
async def getTagList(is_admin: bool = Depends(is_admin_user)):
    if not is_admin:
        tagList = await Tag.exclude(name='Think').order_by('created_at')
    else:
        tagList = await Tag.all()
    return tagList
