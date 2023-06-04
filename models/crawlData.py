from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime


class CrawlDataSchema(BaseModel):
    id: int = Field(..., description="Auto-incrementing ID")
    siteId: str
    url: str
    data: Dict
    timestamp: datetime

    class Config:
        orm_mode = True


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
