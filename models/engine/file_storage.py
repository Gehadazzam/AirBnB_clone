#!/usr/bin/python3
"""Write a class FileStorage that defines all common attributes/methods for other classes"""

import datetime as dt
import json
from os.path import exists
from models.user import User

class FileStorage:
    """class FileStorage that serializes and deserializes JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects in memory"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            s = {k: v for k, v in self.__objects.items()}
            json.dump(s, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if exists (self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                l = json.load(f)
                self.__objects = l
        else:
            return
        
    def cls(self):
        """return a dictionery of classes"""
        
        return {"User": User}
