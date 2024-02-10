#!/usr/bin/python3
"""
Unnitesst for BASEMODEL class
"""


import os
import models
import unittest
from datetime import datetime as dt
from time import sleep
from models.base_model import BaseModel as BM

class testBaseModel(unittest.TestCase):

    def testtype(self):
        #self.assertEqual(BM, type(BM))
        self.assertEqual(str, type(BM().id))
        self.assertEqual(dt, type(BM().created_at))
        self.assertEqual(dt, type(BM().updated_at))


if __name__ == "__main__":
    unittest.main()