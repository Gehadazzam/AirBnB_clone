#!/usr/bin/python3
"""
Unnitesst for BASEMODEL class
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.review import Review as r
from models.base_model import BaseModel as BM

class ReviewTest(unittest.TestCase):

    def testtype(self):
        ex1 = r()
        self.assertEqual(str(type(ex1)), "<class 'models.review.Review'>")
        self.assertIsInstance(ex1, r)
        self.assertTrue(issubclass(type(ex1), BM))
        self.assertEqual(str, type(r().id))
        self.assertEqual(dt, type(r().created_at))
        self.assertEqual(dt, type(r().updated_at))
        