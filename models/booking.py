#!./venv/bin/python
"""
This script defines a Booking class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base as B
from sqlalchemy import Column, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship


# Define the Booking class
class Booking(BaseModel, B):

    # Define the table name for the class
    __tablename__ = 'bookings'

    """
    A class representing a booking, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the person making the booking.
    - email (str): The email address of the person making the booking.
    - phone (str): The phone number of the person making the booking.
    - address (str): The address of the person making the booking.
    - city (str): The city of the person making the booking.
    - country (str): The country of the person making the booking.
    - start_date (Date): The start date of the booking.
    - end_date (Date): The end date of the booking.
    - car_model_id (str): The ID of the car model associated with the booking.
    - amount (float): The amount of the booking.
    """

    # Define the columns for the table
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)  
    phone = Column(String(20), nullable=False)  
    address = Column(String(128), nullable=False)  
    city = Column(String(128), nullable=False)  
    country = Column(String(128), nullable=False)  
    start_date = Column(Date, nullable=False)  
    end_date = Column(Date, nullable=False)  
    car_model_id = Column(String(60), ForeignKey('car_models.id'), nullable=False)  
    amount = Column(Float, nullable=False) 
   
