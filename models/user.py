#!/usr/bin/python3
"""This is a module to defines a class User"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This is a class to defines a user by various attributes"""
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
