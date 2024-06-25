#!/usr/bin/python3
"""
This script defines a Booking class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base as B
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Booking(BaseModel, B):
    __tablename__ = 'bookings'
    """
    A class representing a booking, inheriting from BaseModel.

    Attributes:
    - car_model_id (str): The ID of the car model associated with the booking.
    - user_id (str): The ID of the user who made the booking.
    - start_date (str): The start date of the booking.
    - end_date (str): The end date of the booking.
    - total_price (float): The total price of the booking.
    """
    car_model_id = Column(String(60), ForeignKey('car_models.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    start_date = Column(String(128), nullable=False)
    end_date = Column(String(128), nullable=False)
    total_price = Column(Float, nullable=False)
    reviews = relationship("Review", backref="booking")    
    
   
