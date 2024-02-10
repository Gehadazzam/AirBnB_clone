#!/usr/bin/python3
"""
Unnitesst for BASEMODEL class
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.city import City as c
from models.base_model import BaseModel as BM

class CityTest(unittest.TestCase):

    def testtype(self):
        ex1 = c()
        self.assertEqual(str(type(ex1)), "<class 'models.city.City'>")
        self.assertIsInstance(ex1, c)
        self.assertTrue(issubclass(type(ex1), BM))
        self.assertEqual(str, type(c().id))
        self.assertEqual(dt, type(c().created_at))
        self.assertEqual(dt, type(c().updated_at))
        
    def testmethods(self):
        ex2 = c()
        new_ex2 = ex2.updated_at
        ex2.save()
        self.assertLess(new_ex2, ex2.updated_at)

if __name__ == "__main__":
    unittest.main()
        