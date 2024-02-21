from enum import Enum
from fastapi import APIRouter, HTTPException
from models.models import User
from pydantic import BaseModel, validator, EmailStr
from core.Authenticate import SECRET_KEY, ALGORITHM
import jwt
from typing import Optional

userRouter = APIRouter()

class UserValidator(BaseModel):
    nickname: str
    email: EmailStr

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class Token(BaseModel):
    access_token: Optional[str] = None
    token_type: Optional[str] = None

class UserOut(BaseModel):
    nickname: str
    email: EmailStr
    role: RoleEnum = 'user'
    token: Optional[Token] = None

def model_add_token(user: User, role: RoleEnum):
    token_data = {"role":role, "nickname":user.nickname, "email":user.email}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    user_dict = user.to_dict()
    user_dict["role"] = role
    user_dict["token"] = {"access_token": token, "token_type": "bearer"}
    return user_dict

@userRouter.put('',response_model=UserOut, summary="用户创建/登录",description="检查用户邮箱是否存在，存在则更新昵称，不存在则创建新用户")
async def createUser(userInfo: UserValidator):
    # 检查昵称是否已存在,唯一性约束
    user_by_nickname = await User.filter(nickname=userInfo.nickname).first()
    if user_by_nickname and user_by_nickname.email != userInfo.email:
        raise HTTPException(status_code=400, detail="昵称重复，请选择其他昵称")
    
    registered = await User.filter(email = userInfo.email).first()
    if registered:    
        if registered.id == 1:
            if registered.nickname != userInfo.nickname:
                raise HTTPException(status_code=400, detail="登录失败" )
            # 在这里设置 role 为 admin
            return model_add_token(registered, "admin")
        # 如果数据库中已经存在与 registered 对象相同的记录（通过 email 查找的记录），那么这将更新该记录的 nickname 字段的值。
        registered.nickname = userInfo.nickname
        await registered.save()
        return model_add_token(registered, "user")
    else:
        newUser = await User.create(nickname = userInfo.nickname, email = userInfo.email)
        return model_add_token(newUser, "user")

# @userRouter.put('/{blog_id}')
# async def createArticle(blog_id: int, blog: UserValidator):
#     await User.filter(id = blog_id).update(title = blog.title, content = blog.content)
#     return blog
