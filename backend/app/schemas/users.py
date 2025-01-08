from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    role: str


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
