from fastapi import APIRouter
from models.models import User
from pydantic import BaseModel, validator
userRouter = APIRouter()

class UserValidator(BaseModel):
    nickname: str
    email: str


@userRouter.put('',summary="用户创建/登录",description="检查用户邮箱是否存在，存在则更新昵称，不存在则创建新用户")
async def createUser(userInfo: UserValidator):
    registered = await User.filter(email = userInfo.email)
    # 如果数据库中已经存在与 registered 对象相同的记录（通过 email 查找的记录），那么这将更新该记录的 nickname 字段的值。
    if registered:
        registered = registered[0]
        registered.nickname = userInfo.nickname
        await registered.save() # 更新已存在的对象，而不是插入新数据
        return registered
    else:
        newUser = await User.create(nickname = userInfo.nickname, email = userInfo.email)
        return newUser

# @userRouter.put('/{blog_id}')
# async def createArticle(blog_id: int, blog: UserValidator):
#     await User.filter(id = blog_id).update(title = blog.title, content = blog.content)
#     return blog
