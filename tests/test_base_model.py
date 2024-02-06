#!/usr/bin/python3
import unittest
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from models.engine import file_storage as fs
from models.base_model import BaseModel as bm
import datetime as datetime
import uuid
class BaseModelTest(unittest.TestCase):
    """test the base model"""


    def setup(self):
        pass

    def tearDown(self):
        return super().tearDown()
    
    def test_with_zero_args(self):
        ex1 = bm()
        self.assertEqual(bm, type(ex1))
       

    def test_with_one_argument(self):
        ex2 = bm(ar1 = "Hello")
        self.assertEqual(bm, type(ex2))
        self.assertEqual(ex2.ar1, "Hello")
        #self.assertIsInstance(ex2.id, str)
        #self.assertIs(type(ex2.created_at), datetime)
        #self.assertIsInstance(ex2.updated_at, datetime)

    def test_uuid(self):
        ex3 = bm()
        ex4 = bm()
        self.assertNotEqual(ex3, ex4)
    
    def test__str__(self):
        ex5 = bm()
        string = f"[{ex5.__class__.__name__}] ({ex5.id}) {ex5.__dict__}"
        self.assertEqual(ex5.__str__() ,string)

if __name__ == "__main__":
    unittest.main()
