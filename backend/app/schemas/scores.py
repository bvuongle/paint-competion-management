from pydantic import BaseModel
from typing import Optional


class ScoreCreate(BaseModel):
    participant_id: int
    jury_id: int
    stage_id: int
    points: float
    comments: Optional[str] = None
    is_final: bool = False


class ScoreRead(BaseModel):
    id: int
    participant_id: int
    jury_id: int
    stage_id: int
    points: float
    is_final: bool
    comments: Optional[str] = None

    class Config:
        orm_mode = True
