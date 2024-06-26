#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    """ User class inherits BaseModel and Base """
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    
    def __init__(self, *args, **kwargs):
        """ Initializes a new user """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ Returns a string representation of the instance """
        return "[{} ({}) {}]".format(type(self).__name__, self.id, self.to_dict())