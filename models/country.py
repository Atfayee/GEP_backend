# models/country.py

from sqlalchemy import Column, String
from sqlalchemy.orm import Relationship

from . import Base
from models.model import Model

class Country(Base):
    __tablename__ = "countries"
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    models = Relationship("Model", back_populates="country")

