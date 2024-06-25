#!/usr/bin/python3
"""
This script defines a Review class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    """
    A class representing a review, inheriting from BaseModel.

    Attributes:
    - car_model_id (str): The ID of the car model associated with the review.
    - booking_id (str): The ID of the booking associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.
    - rating (int): The rating of the review.
    """
    car_model_id = Column(String(60), ForeignKey('car_models.id'), nullable=False)
    booking_id = Column(String(60), ForeignKey('bookings.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)