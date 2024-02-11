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
from models.engine.file_storage import FileStorage as FS
from models import storage

class testBaseModel(unittest.TestCase):
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "count")
        except IOError:
            pass
        FS._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("count", "file.json")
        except IOError:
            pass

    def testtype(self):
        # self.assertEqual(BM, type(BM))
        self.assertEqual(str, type(BM().id))
        self.assertEqual(dt, type(BM().created_at))
        self.assertEqual(dt, type(BM().updated_at))

        ex1 = BM()
        sleep(0.05)
        new = ex1.updated_at
        ex1.save()
        sec = ex1.updated_at
        self.assertLess(new, sec)
        sleep(0.05)
        ex1.save()
        self.assertLess(sec, ex1.updated_at)

        ex2 = BM()
        sleep(0.05)
        new = ex2.updated_at
        ex2.save()
        self.assertLess(new, ex2.updated_at)

        ex3 = BM("7", id="64553")
        self.assertEqual(ex3.id, "64553")

        ex4 = BM()
        self.assertIn("id", ex4.to_dict())
        self.assertIn("created_at", ex4.to_dict())
        self.assertIn("updated_at", ex4.to_dict())

        ex5 = BM()
        ex5.name = "Egypt"
        ex5.my_number = 98
        self.assertIn("name", ex5.to_dict())
        self.assertIn("my_number", ex5.to_dict())


        ex6 = BM()
        with self.assertRaises(TypeError):
            ex6.save(None)

        attr = storage.attribe()["BaseModel"]
        ex7 = BM()
        for key, value in attr.items():
            self.assertTrue(hasattr(ex7, key))
            self.assertEqual(type(getattr(ex7, key, None)), value)


if __name__ == "__main__":
    unittest.main()
