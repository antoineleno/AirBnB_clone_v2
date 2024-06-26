#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
import os



class Place(BaseModel, Base):
    """ A place to stay 
        Mapping class for places table
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.user import User
        from models.city import City
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete-orphan")
    else:
        from models import storage
        from models import Review
        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id equals
            to the current Place.id => It will be the FileStorage
            relationship between Place and Review
            """
            return [review for review in storage.all(Review).values()
                     if self.id == Review.place_id]
