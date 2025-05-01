# models/model.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import Relationship
from . import Base

class Model(Base):
    __tablename__ = "models"
    id = Column(String, primary_key=True, nullable=False)
    country_id = Column(String, ForeignKey("countries.id"),nullable=False)
    description = Column(String)

    country = Relationship("Country", back_populates="models")



