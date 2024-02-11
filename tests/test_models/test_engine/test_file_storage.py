#!/usr/bin/python3
"""
Module test for
"""
import os
import json
import models
import unittest
from datetime import datetime as dt
from models.base_model import BaseModel as BM
from models.engine.file_storage import FileStorage as FS
from models.user import User as U
from models.state import State as S
from models.place import Place as P
from models.city import City as C
from models.amenity import Amenity as A
from models.review import Review as R
from models import storage

class FileStorageTest(unittest.TestCase):
    """test store classes"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "count")
        except IOError:
            pass
        FS._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("count", "file.json")
        except IOError:
            pass

    def teststore(self):
        self.assertIsInstance(models.storage, FS)

    def testclass(self):
        ex1, ex2, ex3, ex4, ex5, ex6, ex7 = BM(), A(), U(), R(), P(), S(), C()

        ex3.id = "8765"
        ex3.first_name = "Gehad"

        models.storage.new(ex1)
        models.storage.new(ex2)
        models.storage.new(ex3)
        models.storage.new(ex4)
        models.storage.new(ex5)
        models.storage.new(ex6)
        models.storage.new(ex7)
        models.storage.reload()
        self.assertIn(ex1, models.storage.all().values())
        self.assertIn(ex2, models.storage.all().values())
        self.assertIn(ex3, models.storage.all().values())
        self.assertIn(ex4, models.storage.all().values())
        self.assertIn(ex5, models.storage.all().values())
        self.assertIn(ex6, models.storage.all().values())
        self.assertIn(ex7, models.storage.all().values())

        self.assertIn("BaseModel." + ex1.id, models.storage.all().keys())
        self.assertIn("Amenity." + ex2.id, models.storage.all().keys())
        self.assertIn("User." + ex3.id, models.storage.all().keys())
        self.assertIn("Review." + ex4.id, models.storage.all().keys())
        self.assertIn("Place." + ex5.id, models.storage.all().keys())
        self.assertIn("State." + ex6.id, models.storage.all().keys())
        self.assertIn("City." + ex7.id, models.storage.all().keys())

        attr = storage.all()
        k = ex3.__class__.__name__ + "." + str(ex3.id)
        self.assertIsNotNone(attr[k])
        self.assertEqual(type(attr), dict)
        self.assertIs(attr, storage._FileStorage__objects)
        

        
if __name__ == "__main__":
    unittest.main()
