#!/usr/bin/python3
"""Write a class BaseModel that defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime

class BaseModel:
    """all function in basemodel class"""
    def __init__(self):
        """id / created_at / updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """should print: {[<class name>] (<self.id>) <self.__dict__>}"""
        return ("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at =  datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        my_ob_dict = self.__dict__.copy()
        my_ob_dict["__class__"] = self.__class__.__name__
        my_ob_dict["created_at"] = self.created_at.isoformat()
        my_ob_dict["updated_at"] = self.updated_at.isoformat()
        return my_ob_dict

