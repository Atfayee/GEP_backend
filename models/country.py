# models/country.py

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from . import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    models = relationship("Model", back_populates="country", cascade="all, delete-orphan")

