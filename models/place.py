#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
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
    amenity_ids = []

    place_amenity = Table ('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)                             
    )

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.user import User
        from models.city import City
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity, back_populates='place_amenities', viewonly=False)
    else:
        from models import storage
        from models.review import Review
        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id equals
            to the current Place.id => It will be the FileStorage
            relationship between Place and Review
            """
            return [review for review in storage.all(Review).values()
                     if self.id == Review.place_id]
        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            """
            returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id linked to the Place
            """
            return [amenity for amenity in storage.all(Amenity).values() if amenity.id in self.amenity_ids ]
        @amenities.setter
        def amenities(self, obj):
            from models.amenity import Amenity
            """
            handles append method for adding an Amenity.id to the attribute amenity_ids.
              This method should accept only Amenity object, otherwise, do nothing.
            """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
