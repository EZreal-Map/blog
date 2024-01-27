# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: app运行时文件
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from api.blog import blogRouter
from api.user import userRouter
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException
from core.Middleware import Middleware
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
    )


# 事件监听
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))


# 异常错误处理
application.add_exception_handler(HTTPException, http_error_handler) # HTTP异常重写
application.add_exception_handler(RequestValidationError, http422_error_handler) # 请求验证错误
application.add_exception_handler(UnicornException, unicorn_exception_handler) # web服务器错误

# 路由
application.include_router(blogRouter, prefix="/blog")
application.include_router(userRouter, prefix="/user")


# 中间件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key="session",
    session_cookie="f_id",
    # max_age=4
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

TORTOISE_ORM = settings.TORTOISE_ORM  # 数据库配置 aerich init -t main.TORTOISE_ORM
register_tortoise(
    application,
    config = TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

# 静态资源目录
application.mount('/static', StaticFiles(directory=os.path.join(os.getcwd(), "static")))

app = application

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)