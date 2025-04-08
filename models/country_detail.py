from typing import List, Optional, Union
from pydantic import BaseModel

class FilterRange(BaseModel):
    min: float
    max: float

class FilterOption(BaseModel):
    id: int
    value: Union[str, int, float]
    label: str

class Filter(BaseModel):
    id: int
    key: str
    label: str
    timestep: bool
    type: str
    range: Optional[FilterRange] = None
    options: Optional[List[FilterOption]] = None

class LeverOption(BaseModel):
    id: int
    value: str

class Lever(BaseModel):
    id: int
    label: str
    description: str
    options: List[LeverOption]
    default: Optional[int] = None

class Attribution(BaseModel):
    author: str
    url: str

class Model(BaseModel):
    id: str
    country: str
    attribution: Attribution
    description: str
    disclaimer: Optional[str]
    filters: List[Filter]
    levers: List[Lever]
    timesteps: List[int]
    baseYear: int

class CountryDetail(BaseModel):
    id: str
    name: str
    models: List[Model]