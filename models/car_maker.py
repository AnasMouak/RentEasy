#!./venv/bin/python
"""
This script defines a CarMaker class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel ,Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Define the CarMaker class
class CarMaker(BaseModel, Base):

    # Define the table name for the class
    __tablename__ = 'car_makers'
    """
    A class representing a car maker, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the car maker.
    """

    # Define the columns for the table
    name = Column(String(128), nullable=False)

    # Define the relationship between CarMaker and CarModel
    car_models = relationship("CarModel", backref="car_maker", cascade="all, delete-orphan")

    @property
    def car_models(self):
        """
        Getter attribute that returns the list of CarModel instances
        with car_maker_id equals to the current CarMaker.id.
        """
        from models import storage
        from models.car_model import CarModel
        car_models = []
        # Iterate over all CarModel instances and collect those related to this CarMaker
        for car_model in storage.all(CarModel).values():
            if car_model.car_maker_id == self.id:
                car_models.append(car_model)
        
        return car_models
