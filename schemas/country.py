# schemas/country.py
from pydantic import BaseModel

class Country(BaseModel):
    id: str
    name: str


