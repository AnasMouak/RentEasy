#!/usr/bin/python3
"""
This script defines a CarMaker class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class CarMaker(BaseModel):
    """
    A class representing a car maker, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the car maker.
    """
    name = ""
