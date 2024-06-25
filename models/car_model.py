#!/usr/bin/python3
"""
This script defines a CarModel class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class CarModel(BaseModel):
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

    car_maker_id = ""
    name = ""
    price_per_day = 0.0
    kilometers = 0.0
    year = 0
    color = ""
    passengers = 0
    doors = 0
    transmission = ""
    fuel = ""
