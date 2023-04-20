#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from os import getenv
from models.amenity import Amenity
from models.review import Review
import models
import os

place_amenity = Table('place_amenity',Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)

"""
Represents the many to many relationship table
between Place and Amenity records.
"""
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(String(1024), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []
    reviews = relationship(
        'Review',
        cascade="all, delete, delete-orphan",
        backref='place'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities'
        )
    else:
        @property
        def amenities(self):
            """Returns the amenities of this Place"""
            from models import storage
            amenities_of_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_of_place.append(value)
            return amenities_of_place

        @amenities.setter
        def amenities(self, value):
            """Adds an amenity to this Place"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Returns the reviews of this Place"""
            from models import storage
            reviews_of_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place


# table = Table("place_amenity", Base.metadata, Column("place_id", String(60),
#               ForeignKey("places_id"),  primary_key=True, nullable=False),
#               Column("amenity_id", String(60),
#               ForeignKey("amenities.id"), primary_key=True, nullable=False))


# class Place(BaseModel, Base):
#     __tablename__ = "places"
#     city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
#     user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
#     name = Column(String(128), nullable=False)
#     description = Column(String(1024), nullable=True)
#     number_rooms = Column(Integer, default=0, nullable=False)
#     number_bathrooms = Column(Integer, default=0, nullable=False)
#     max_guest = Column(Integer, default=0, nullable=False)
#     price_by_night = Column(Integer, default=0, nullable=False)
#     latitude = Column(Float, nullable=True)
#     longitude = Column(Float, nullable=True)
#     reviews = relationship("Review", backref="place", cascade="delete")
#     amenities = relationship("Amenity", secondary="place_amenity",
#                              viewonly=False)
#     amenity_ids = []

#     if getenv("HBNB_TYPE_STORAGE", None) != "db":
#         @property
#         def reviews(self):
#             """
#             Get a list of all linked Reviews.
#             """
#             review_list = []
#             for review in list(models.storage.all(Review).values()):
#                 if review.place_id == self.id:
#                     review_list.append(review)
#             return review_list

#         @property
#         def amenities(self):
#             """
#             Get or set linked Amenities.
#             """
#             amenity_list = []
#             for amenity in list(models.storage.all(Amenity).values()):
#                 if amenity.id in self.amenity_ids:
#                     amenity_list.append(amenity)
#             return amenity_list

#         @amenities.setter
#         def amenities(self, value):
#             if type(value) == Amenity:
#                 self.amenity_ids.append(value.id)
