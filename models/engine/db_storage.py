#!./venv/bin/python
"""
This script defines a DBStorage class.
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.car_maker import CarMaker
from models.car_model import CarModel
from models.booking import Booking
from models.review import Review
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    A class representing a database storage system.

    Attributes:
    - __engine : engine
    - __session : session object
    """
    __engine = None
    __session = None

    def __init__(self):
        """Create SQLAlchemy engine
        """
        self.__engine = create_engine('mariadb+mariadbconnector://{}:{}@{}/{}'
                                      .format(getenv('RENTEASY_MYSQL_USER'),
                                              getenv('RENTEASY_MYSQL_PWD'),
                                              getenv('RENTEASY_MYSQL_HOST'),
                                              getenv('RENTEASY_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('RENTEASY_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query and return all objects by class/generally
        Return: dictionary (<class-name>.<object-id>: <obj>)
        """
        cls_objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                cls_objects[f"{cls.__name__}.{obj.id}"] = obj
        else:
            for c in [CarMaker, User, CarModel, Booking, Review]:
                for obj in self.__session.query(c).all():
                    cls_objects[f"{c.__name__}.{obj.id}"] = obj
        return cls_objects

    def new(self, obj):
        """Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create database session
        """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess)

    def close(self):
        """Close current session
        """
        self.__session.remove()