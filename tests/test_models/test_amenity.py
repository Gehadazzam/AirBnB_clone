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
        self.assertless(new_ex2, ex2.updated_at)
        