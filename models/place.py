#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
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

    metadata = Base.metadata

    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True,
                                 nullable=False)
                          )

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False, overlaps="place_amenities")

    else:
        @property
        def reviews(self):
            """Returns the list of Review instances"""
            reviews_instances = []

            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_instances.append(review)
            return reviews_instances

        @property
        def amenities(self):
            """Returns the list of Amenities instances"""
            amenities_instances = []

            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities_instances.append(amenity)
            return amenities_instances

        @amenities.setter
        def amenities(self, obj):
            """Amenities setter method"""
            if type(obj) is Amenity():
                self.amenity_ids.append(obj)
