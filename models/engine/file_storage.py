#!/usr/bin/python3
"""Write a class FileStorage that defines all common attributes/methods for other classes"""

import datetime as dt
from os.path import exists
<<<<<<< HEAD
from models.user import User
=======
import json
import datetime
import os
>>>>>>> g-feature

class FileStorage:
    """class FileStorage that serializes and deserializes JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects in memory"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            s = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(s, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if exists (FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                l = json.load(f)
                l = {k: self.class_dict()[v["__class__"]](**v)
                        for k, v in l.items()}
                FileStorage.__objects = l
        else:
            return
<<<<<<< HEAD
        
    def cls(self):
        """return a dictionery of classes"""
        
        return {"User": User}
=======

    def class_dict(self):
        """to correctly serialize and deserialize instances of the new classes"""
        from models.base_model import BaseModel
        from models.user  import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return class_dict

    def attribe(self):
        """Returns the valid attributes and their types for classname"""
        attribe = {
            "BaseModel":
                    {"id": str,
                     "created_at": dt.datetime,
                     "updated_at": dt.datetime},
            "User":
                    {"email": str,
                     "password": str,
                     "first_name": str,
                     "last_name": str},
            "State":
                    {"name": str},
            "City":
                    {"state_id": str,
                     "name": str},
            "Amenity":
                    {"name": str},
            "Place":
                    {"city_id": str,
                     "user_id": str,
                     "name": str,
                     "description": str,
                     "number_rooms": int,
                     "number_bathrooms": int,
                     "max_guest": int,
                     "price_by_night": int,
                     "latitude": float,
                     "longitude": float,
                     "amenity_ids": list},
            "Review":
                    {"place_id": str,
                     "user_id": str,
                     "text": str}
        }
        return attribe
>>>>>>> g-feature
