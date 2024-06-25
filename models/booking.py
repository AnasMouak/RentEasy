#!/usr/bin/python3
"""
This script defines a Booking class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Booking(BaseModel):
    """
    A class representing a booking, inheriting from BaseModel.

    Attributes:
    - car_model_id (str): The ID of the car model associated with the booking.
    - user_id (str): The ID of the user who made the booking.
    - start_date (str): The start date of the booking.
    - end_date (str): The end date of the booking.
    - total_price (float): The total price of the booking.
    """
    car_model_id = ""
    user_id = ""
    start_date = ""
    end_date = ""
    total_price = 0.0
    
   
