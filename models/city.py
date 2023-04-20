#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import os

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # if storage_type == 'db':
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    # else:
    #     name = ''
    #     state_id = ''
