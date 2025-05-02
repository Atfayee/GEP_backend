from pydantic import BaseModel
from typing import List


class LeverOut(BaseModel):
    id: int
    label: str
    description: str
    class Config:
        orm_mode = True


class ModelOut(BaseModel):
    id: str
    country_id: str
    description: str
    levers: List[LeverOut] = []

    class Config:
        orm_mode = True
    