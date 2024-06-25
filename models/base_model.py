#!/usr/bin/python3
"""
This script defines a BaseModel class that serves as the base class for other models.
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    A class representing a base model for other models.

    Attributes:
    - id (str): The unique identifier for the model instance.
    - created_at (datetime): The datetime when the instance was created.
    - updated_at (datetime): The datetime when the instance was last updated.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        If kwargs is not empty, it loads data from kwargs. Otherwise, it generates
        a new id and sets the created_at and updated_at attributes to the current time.
        """
        if not kwargs:
            uid = uuid.uuid4()
            self.id = str(uid)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], 
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], 
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)


    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Updates the updated_at attribute to the current time and saves the instance."""
        now = datetime.now()
        self.updated_at = now
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
        - dict: A dictionary representation of the BaseModel instance.
        """
        dict = {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
        }
        for key, value in self.__dict__.items():
            if key not in dict:
                dict[key] = value
        return dict
