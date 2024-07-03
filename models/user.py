#!/usr/bin/python3
"""
This script defines a User class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = 'users'
    """
    A class representing a user, inheriting from BaseModel.

    Attributes:
    - email (str): The email address of the user.
    - password (str): The password of the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    - bookings (list): A list of Booking instances associated with the user.
    - reviews (list): A list of Review instances written by the user.
    """

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    reviews = relationship("Review", backref="user")

