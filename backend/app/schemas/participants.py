from pydantic import BaseModel
from typing import Optional
from datetime import date


class ParticipantCreate(BaseModel):
    user_id: int
    school_id: Optional[int] = None
    first_name: str
    last_name: str
    birthdate: Optional[date] = None
    chosen_topic: Optional[str] = None


class ParticipantRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    chosen_topic: Optional[str] = None

    class Config:
        orm_mode = True
