#!/usr/bin/python3
"""
This script defines a CarMaker class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel ,Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.car_model import CarModel
from models import storage


class CarMaker(BaseModel, Base):
    __tablename__ = 'car_makers'
    """
    A class representing a car maker, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the car maker.
    """
    name = Column(String(128), nullable=False)
    car_models = relationship("CarModel", backref="car_maker")

    @property
    def car_models(self):
        """
        Getter attribute that returns the list of CarModel instances
        with car_maker_id equals to the current CarMaker.id.
        """

        car_models = []
        for car_model in storage.all(CarModel).values():
            if car_model.car_maker_id == self.id:
                car_models.append(car_model)
        
        return car_models
