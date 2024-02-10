#!/usr/bin/python3
"""
module using unittest to test our command interpreter
"""


import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand as HB
from io import StringIO as SO
from unittest.mock import patch


class Test_HBNBCommand(unittest.TestCase):
    """test the command interpreter"""

    def test_help(self):

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help"))
           output = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
           self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help quit"))
           output = "quit the command interpreter"
           self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help update"))
           output = """Updates an instance adding or updating attribute"""
           self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help all"))
           output = """Prints all string representation of all instances"""
           self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help count"))
           output = """retrive the number of instances of a class"""
           self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help destroy"))
           output = """if the class exist destroy it"""
           self.assertEqual(output, test.getvalue().strip())
        
        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help show"))
           output = """Prints the string representation the class name and id"""
           self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help create"))
           output = """Creates a new instance of BaseModel"""
           self.assertEqual(output, test.getvalue().strip())

        #with patch("sys.stdout", new=SO()) as test:
         #  self.assertFalse(HB().onecmd("help emptyline"))
          # output = """nothing just pass"""
           #self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("help EOF"))
           output = """print new line and exit"""
           self.assertEqual(output, test.getvalue().strip())


    def test_EOF(self):
        
        with patch("sys.stdout", new=SO()) as test:
           self.assertTrue(HB().onecmd("EOF"))

    def test_quit(self):
        
        with patch("sys.stdout", new=SO()) as test:
           self.assertTrue(HB().onecmd("quit"))

    def test_empty_line(self):        
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd(""))
            self.assertEqual("", test.getvalue().strip())

    def test_create(self):
       
        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("create"))
           output = "** class name missing **"
           self.assertEqual(output, test.getvalue().strip())
           
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create USER"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("USER.create()"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())

    def test_show(self):
        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("show"))
           output = "** class name missing **"
           self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show USER"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("USER.show()"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show User"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create User"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["User.{}".format(id_attribute)]
            cmd = "User.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create BaseModel"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["BaseModel.{}".format(id_attribute)]
            cmd = "BaseModel.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create Place"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["Place.{}".format(id_attribute)]
            cmd = "Place.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create Amenity"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["Amenity.{}".format(id_attribute)]
            cmd = "Amenity.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create Review"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["Review.{}".format(id_attribute)]
            cmd = "Review.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create City"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["City.{}".format(id_attribute)]
            cmd = "City.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create State"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["State.{}".format(id_attribute)]
            cmd = "State.show({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())


    def test_update(self):
        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("update"))
           output = "** class name missing **"
           self.assertEqual(output, test.getvalue().strip())    
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update USER"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update User"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())


    def test_destroy(self):
        with patch("sys.stdout", new=SO()) as test:
           self.assertFalse(HB().onecmd("destroy"))
           output = "** class name missing **"
           self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy USER"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("USER.destroy()"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy User"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create User"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["User.{}".format(id_attribute)]
            cmd = "User.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create BaseModel"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["BaseModel.{}".format(id_attribute)]
            cmd = "BaseModel.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create Place"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["Place.{}".format(id_attribute)]
            cmd = "Place.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create Amenity"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["Amenity.{}".format(id_attribute)]
            cmd = "Amenity.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create Review"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["Review.{}".format(id_attribute)]
            cmd = "Review.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create City"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["City.{}".format(id_attribute)]
            cmd = "City.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("create State"))
            id_attribute = test.getvalue().strip()
        with patch("sys.stdout", new=SO()) as test:
            cls = storage.all()["State.{}".format(id_attribute)]
            cmd = "State.destroy({})".format(id_attribute)
            self.assertFalse(HB().onecmd(cmd))
            self.assertNotIn(cls, storage.all())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())


    def test_all(self):
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all USER"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("USER.all()"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.all()"))
            self.assertIn("Amenity", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all Amenity"))
            self.assertIn("Amenity", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all BaseModel"))
            self.assertIn("BaseModel", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.all()"))
            self.assertIn("City", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all City"))
            self.assertIn("City", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.all()"))
            self.assertIn("Place", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all Place"))
            self.assertIn("Place", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.all()"))
            self.assertIn("Review", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all Review"))
            self.assertIn("Review", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.all()"))
            self.assertIn("State", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all State"))
            self.assertIn("State", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.all()"))
            self.assertIn("User", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("all User"))
            self.assertIn("User", test.getvalue().strip())
if __name__ == "__main__":
    unittest.main()