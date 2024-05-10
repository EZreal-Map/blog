from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
from fastapi import Depends, HTTPException


SECRET_KEY = "ioweurlaksjdfoiquwerlkasjdf"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user",auto_error=False)


def is_admin_user(token: str = Depends(oauth2_scheme)) -> bool:
    # print("is_admin_user", token)
    if not token:
        return False  # 如果没有提供 token，直接返回 False
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("role") != "admin":
            raise HTTPException(status_code=403, detail="权限不足")
        return True
    except Exception as e:  # 捕获所有异常
        # 记录异常信息或者进行其他错误处理
        print(f"Error decoding token: {str(e)}")
        return False
