#!/usr/bin/python3
"""Write a class BaseModel that defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime as dt
from models import storage

class BaseModel:
    """all function in basemodel class"""

    def __init__(self, *args, **kwargs):
        """id / created_at / updated_at"""
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = dt.strptime(kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:    
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """should print: {[<class name>] (<self.id>) <self.__dict__>}"""

        return ("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current dt"""

        self.updated_at =  dt.now()
        storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        my_ob_dict = self.__dict__.copy()
        my_ob_dict["__class__"] = self.__class__.__name__
        my_ob_dict["created_at"] = my_ob_dict["updated_at"].isoformat()
        my_ob_dict["updated_at"] = my_ob_dict["updated_at"].isoformat()
        return my_ob_dict

