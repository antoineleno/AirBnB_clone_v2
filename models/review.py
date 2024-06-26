#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
#from models.place import Place
#from models.user import User


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    #place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    #user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initializes a new user """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ Returns a string representation of the instance """
        return "[{} ({}) {}]".format(type(self).__name__, self.id, self.to_dict())