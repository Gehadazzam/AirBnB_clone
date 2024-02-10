#!/usr/bin/python3
"""
Unnitesst for BASEMODEL class
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.place import Place as p
from models.base_model import BaseModel as BM

class TestPlace(unittest.TestCase):

    def testtype(self):
        ex1 = p()
        self.assertEqual(str(type(ex1)), "<class 'models.place.Place'>")
        self.assertIsInstance(ex1, p)
        self.assertTrue(issubclass(type(ex1), BM))
        self.assertEqual(str, type(p().id))
        self.assertEqual(dt, type(p().created_at))
        self.assertEqual(dt, type(p().updated_at))
        
    def testmethods(self):
        ex2 = p()
        new_ex2 = ex2.updated_at
        ex2.save()
        self.assertLess(new_ex2, ex2.updated_at)
        

if __name__ == "__main__":
    unittest.main()