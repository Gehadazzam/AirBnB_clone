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
from models import storage

class TestState(unittest.TestCase):
    def testtype(self):
        ex1 = s()
        self.assertEqual(str(type(ex1)), "<class 'models.state.State'>")
        self.assertIsInstance(ex1, s)
        self.assertTrue(issubclass(type(ex1), BM))
        self.assertEqual(str, type(s().id))
        self.assertEqual(dt, type(s().created_at))
        self.assertEqual(dt, type(s().updated_at))

    def testmethods(self):
        ex2 = s()
        new_ex2 = ex2.updated_at
        ex2.save()
        self.assertLess(new_ex2, ex2.updated_at)

        attr = storage.attribe()["State"]
        ex7 = s()
        for key, value in attr.items():
            self.assertTrue(hasattr(ex7, key))
            self.assertEqual(type(getattr(ex7, key, None)), value)
if __name__ == "__main__":
    unittest.main()
