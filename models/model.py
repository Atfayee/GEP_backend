# models/model.py
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from . import Base

class Model(Base):
    __tablename__ = "models"
    id = Column(String, primary_key=True, nullable=False)
    country_id = Column(String, ForeignKey("countries.id"), nullable=False)
    description = Column(String)

    country = relationship("Country", back_populates="models")
    levers = relationship("Lever", back_populates="model", cascade="all, delete-orphan")


class Lever(Base):
    __tablename__ = "levers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label = Column(String, nullable=False)
    description = Column(String)
    model_id = Column(String, ForeignKey("models.id"), nullable=False)

    model = relationship("Model", back_populates="levers")

    
