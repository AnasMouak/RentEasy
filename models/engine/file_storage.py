#!/usr/bin/python3
"""
This script defines a FileStorage class .
"""
import json
import os

class FileStorage:
    """
    A class representing a file-based storage system.

    Attributes:
    - __file_path (str): The path to the JSON file used for storing data.
    - __objects (dict): A dictionary containing all stored objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects."""
        return self.__objects
    
    def new(self, obj):
        """Adds a new object to the storage."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """Serializes and saves all objects to the JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            n = json.dumps(serialized_objects)
            f.write(n)
        

    def reload(self):
        """
        Loads objects from the JSON file into memory.

        If the file does not exist or is empty, clears the stored objects.
        """
        if not os.path.exists(self.__file_path):
            self.__objects.clear()  
            return
        
        if os.path.getsize(self.__file_path) == 0:
            self.__objects.clear()  
            return

        from models.base_model import BaseModel
        from models.user import User
        from models.booking import Booking
        from models.car_maker import CarMaker
        from models.car_model import CarModel
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            'User': User,
            'Booking': Booking,
            'CarMaker': CarMaker,
            'CarModel': CarModel,
            'Review': Review
        }

        with open(self.__file_path, 'r', encoding='utf-8') as f:
            obj_dict = json.load(f)

        #self.__objects.clear()  
        for obj_id, obj_data in obj_dict.items():
            class_name = obj_data['__class__']
            if class_name in classes:
                obj_class = classes[class_name]
                obj_instance = obj_class(**obj_data)
                self.all()[obj_id] = obj_instance

    def delete(self, obj=None):
        """Deletes an object from the storage."""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(key, None)
            self.save()
