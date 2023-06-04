from pydantic import BaseModel, Field
from datetime import datetime


class URL(BaseModel):
    id: int = Field(..., description="Auto-incrementing ID")
    url: str = Field(...)
    userID: str = Field(...)
    timestamp: datetime

    class Config:
        orm_mode = True
