# models/country.py
from sqlmodel import SQLModel, Field

class Country(SQLModel, table=True):
    iso: str = Field(primary_key=True)
    name: str
    lat: float
    lng: float
