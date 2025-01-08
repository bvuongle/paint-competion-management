from pydantic import BaseModel


class ThresholdCreate(BaseModel):
    stage_id: int
    min_score: float


class ThresholdRead(BaseModel):
    id: int
    stage_id: int
    min_score: float

    class Config:
        orm_mode = True
