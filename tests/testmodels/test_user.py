#!/usr/bin/python3
"""
Unnitesst for BUserclass
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.user import User as U
from models.base_model import *
class testBaseModel(unittest.TestCase):

    def testtype(self):
        ex1 = U()
        self.assertEqual(str(type(ex1)), "<class 'models.user.User'>")
        self.assertIsInstance(ex1, U)
        self.assertTrue(issubclass(type(ex1), BaseModel))
        self.assertEqual(str, type(U().id))
        self.assertEqual(dt, type(U().created_at))
        self.assertEqual(dt, type(U().updated_at))
        