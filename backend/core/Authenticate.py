from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
from fastapi import Depends, HTTPException


SECRET_KEY = "ioweurlaksjdfoiquwerlkasjdf"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class Token(BaseModel):
    access_token: str
    token_type: str

def is_admin_user(token: str = Depends(oauth2_scheme)):
    print("is_admin_user", token)
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="权限不足")
    return True
