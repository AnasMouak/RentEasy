#!/usr/bin/python3
"""
This script defines a Review class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review, inheriting from BaseModel.

    Attributes:
    - car_model_id (str): The ID of the car model associated with the review.
    - booking_id (str): The ID of the booking associated with the review.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.
    - rating (int): The rating of the review.
    """
    car_model_id = ""
    booking_id = ""
    user_id = ""
    text = ""
    rating = 0
