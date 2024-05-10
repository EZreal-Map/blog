from fastapi import APIRouter, HTTPException
from models.models import Time
from datetime import datetime
from pydantic import BaseModel

class TimeRecord(BaseModel):
    status: str
    start_time: str
    end_time: str

timeRouter = APIRouter()

@timeRouter.post("", response_model=TimeRecord)
async def get_or_create_time_record():
    # 查询最新的时间记录
    latest_time_record = await Time.all().order_by('-start_time').first()
    
    if latest_time_record:
        start_time=latest_time_record.start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time=latest_time_record.end_time.strftime("%Y-%m-%d %H:%M:%S")
        # 如果最新的记录的start_time和end_time不相等
        if start_time != end_time:
            # 创建一个新的时间记录
            new_time_record = await Time.create()
            status = "start"
        else:
            # 修改当前记录的end_time为当前时间
            latest_time_record.end_time = datetime.now()
            await latest_time_record.save()
            status = "end"
            return TimeRecord(
                status=status,
                start_time=start_time,
                end_time=latest_time_record.end_time.strftime("%Y-%m-%d %H:%M:%S")
            )
    else:
        # 如果数据库中没有时间记录，则创建一个新的时间记录
        new_time_record = await Time.create()
        status = "start"

    return TimeRecord(
        status=status,
        start_time=new_time_record.start_time.strftime("%Y-%m-%d %H:%M:%S"),
        end_time=new_time_record.end_time.strftime("%Y-%m-%d %H:%M:%S"),
    )
