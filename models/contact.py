#!./venv/bin/python
"""
This script defines a Contact class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel, Base as B
from sqlalchemy import Column, String

# Define the Contact class
class Contact(BaseModel, B):

    # Define the table name for the class
    __tablename__ = 'contacts'

    """
    A class representing a contact, inheriting from BaseModel.

    Attributes:
    - name (str): The name of the person making the contact.
    - email (str): The email address of the person making the contact.
    - message (str): The message of the person making the contact.
    """
    
    # Define the columns for the table
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)  
    message = Column(String(128), nullable=False)