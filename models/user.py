#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """ User class inherits BaseModel and Base """
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", back_populates="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review", back_populates="user",
                              cascade="all, delete-orphan")

