#!/usr/bin/python3
"""
Unnitesst for Amenity class
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.amenity import Amenity as A
from models.base_model import BaseModel as BM
from models import storage

class testAmenity(unittest.TestCase):
    def testtype(self):
        ex1 = A()
        self.assertEqual(str(type(ex1)), "<class 'models.amenity.Amenity'>")
        
        self.assertIsInstance(ex1, A)
        self.assertTrue(issubclass(type(ex1), BM))
        self.assertEqual(str, type(A().id))
        self.assertEqual(dt, type(A().created_at))
        self.assertEqual(dt, type(A().updated_at))

    def testmethods(self):
        ex2 = A()
        new_ex2 = ex2.updated_at
        ex2.save()
        self.assertLess(new_ex2, ex2.updated_at)


        attr = storage.attribe()["Amenity"]
        ex7 = A()
        for key, value in attr.items():
            self.assertTrue(hasattr(ex7, key))
            self.assertEqual(type(getattr(ex7, key, None)), value)

if __name__ == "__main__":
    unittest.main()
