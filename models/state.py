#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = ''
        cityes = []
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals to the currentState.id => It will be the
            FileStorage relationship between State and City
            """
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
          
