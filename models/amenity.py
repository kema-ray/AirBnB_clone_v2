#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """
    Represents an amenity for MySQL database
    """
    __tablename__ = "amenities"
    name = Column(String(128), 
            nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
    
    # if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
