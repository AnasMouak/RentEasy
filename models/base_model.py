#!./venv/bin/python
"""
This script defines a BaseModel class that serves as the base class for other models.
"""
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """
    A class representing a base model for other models.

    Attributes:
    - id (str): The unique identifier for the model instance.
    - created_at (datetime): The datetime when the instance was created.
    - updated_at (datetime): The datetime when the instance was last updated.
    """

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

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
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
            
            if '__class__' in kwargs:
                del kwargs['__class__']
            
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], 
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], 
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)


    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Updates the updated_at attribute to the current time and saves the instance."""
        from models import storage
        now = datetime.now()
        self.updated_at = now
        storage.new(self)
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

        if '_sa_instance_state' in dict:
            del dict['_sa_instance_state']

        return dict

    def delete(self):
        """
        Deletes the current instance from storage by calling the method delete.
        """
        from models import storage
        storage.delete(self)