#!/usr/bin/Python3
"""This module defines the engine for the MySQL database"""
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
import os

host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')
user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')

class DBStorage:
    """Defining the class DBStorage"""

    __classes = [State, City, User, Place, Review, Amenity]
    __engine = None
    __session = None

    def __init__(self):
        """Contructor for the class DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
    if env == "test":
        Base.MetaData.drop_all()

    def all(self, cls=None):
        """Method to return a dictionary of objects"""
        new_dic = {}
        if cls in self.__classes:
            result = DBStorage.__session.query(cls)
            for rows in result:
                key = "{}.{}".format(rows.__class__.__name__, rows.id)
                new_dic[key] = rows
        elif cls is None:
            for cl in self.__classes:
                result = DBStorage.__session.query(cl)
                for rows in result:
                    key = "{}.{}".format(rows.__class__.__name__, rows.id)
                    new_dic[key] = rows
        return new_dic

    def new(self, obj):
        """Method to add a new object to the current database"""
        DBStorage.__session.add(obj)

    def save(self):
        """Method to commit all changes to the current database"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Method to delete a new object to the current database"""
        DBStorage.__session.delete(obj)

    def reload(self):
        """Method to create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()

    def close(self):
        """public methodto to call remove method"""
        DBStorage.__session.close()
