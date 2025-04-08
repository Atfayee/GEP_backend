from typing import List
from pydantic import BaseModel

class CountrySummary(BaseModel):
    id: str
    name: str

class CountryListResponse(BaseModel):
    countries: List[CountrySummary]