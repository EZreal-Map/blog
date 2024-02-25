from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import platform

imageRouter = APIRouter()

@imageRouter.post('/upload', summary="上传图片", description="上传图片")
async def uploadImage(file: UploadFile = File(...)):
    try:
        # 获取文件名
        filename = file.filename
        print(filename)

        # 判断操作系统
        is_linux = platform.system().lower() == 'linux'

        # 构建保存文件的完整路径
        if is_linux:
            save_path = Path("/usr/share/nginx/blog_images") / filename  # Linux 图片文件保存路径
        else:
            save_path = Path("static/images") / filename  # 直接在相对路径下保存

        # 将文件保存到指定路径
        with open(save_path, "wb") as f:
            f.write(file.file.read())

        return {"filename": filename, "save_path": str(save_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
