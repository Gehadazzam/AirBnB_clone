#!/usr/bin/python3
"""
Unnitesst for BASEMODEL class
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.state import State as s
from models.base_model import BaseModel as BM

class TestState(unittest.TestCase):

    def testtype(self):
        ex1 = s()
        self.assertEqual(str(type(ex1)), "<class 'models.state.State'>")
        self.assertIsInstance(ex1, s)
        self.assertTrue(issubclass(type(ex1), BM))
        self.assertEqual(str, type(s().id))
        self.assertEqual(dt, type(s().created_at))
        self.assertEqual(dt, type(s().updated_at))
        