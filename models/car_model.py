#!./venv/bin/python
"""
This script defines a CarModel class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel ,Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class CarModel(BaseModel, Base):
    __tablename__ = 'car_models'
    """
    A class representing a car model, inheriting from BaseModel.

    Attributes:
    - car_maker_id (str): The ID of the Car Maker associated with the car model.
    - name (str): The name of the car model.
    - price_per_day (float): The price per day of the car model.
    - kilometers (float): The number of kilometers the car model has driven.
    - year (int): The year the car model was manufactured.
    - color (str): The color of the car model.
    - passengers (int): The number of passengers the car model can carry.
    - doors (int): The number of doors the car model has.
    - transmission (str): The type of transmission the car model has.
    - fuel (str): The type of fuel the car model uses.
    """

    car_maker_id = Column(String(60), ForeignKey('car_makers.id'), nullable=False)
    name = Column(String(128), nullable=False)
    price_per_day = Column(Integer, nullable=False)
    kilometers = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False, default=2021)
    color = Column(String(128), nullable=False)
    passengers = Column(Integer, nullable=False, default=4)
    doors = Column(Integer, nullable=False, default=2)
    transmission = Column(String(128), nullable=False)
    fuel = Column(String(128), nullable=False)
    bookings = relationship("Booking", backref="car_model")
    reviews = relationship("Review", backref="car_model")
    

