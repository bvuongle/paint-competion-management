from pydantic import BaseModel
from typing import Optional


class AppealCreate(BaseModel):
    score_id: int
    appeal_text: str


class AppealRead(BaseModel):
    id: int
    score_id: int
    appeal_text: str
    jury_response: Optional[str] = None
    is_resolved: bool = False

    class Config:
        orm_mode = True
