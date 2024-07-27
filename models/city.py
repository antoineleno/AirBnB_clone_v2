#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Mapping class for cities table
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.state import State
        state = relationship("State", back_populates="cities")
        places = relationship("Place", back_populates="cities",
                              cascade="all, delete-orphan")
