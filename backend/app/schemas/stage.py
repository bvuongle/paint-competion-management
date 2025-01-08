from pydantic import BaseModel
from typing import Optional
from datetime import date


class StageCreate(BaseModel):
    name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_active: bool = False


class StageRead(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True
