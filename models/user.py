#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from models import storage_type
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
import os

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(String(128), nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(String(128), nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship('Place', backref='user',
            cascade='delete') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship('Review', backref='user',
            cascade='delete') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    
