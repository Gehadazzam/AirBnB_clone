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

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "count")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

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

    def test_help(self):
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("help"))
            output = (
                "Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update"
            )
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
            output =\
                """Prints the string representation the class name and id"""
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("help create"))
            output = """Creates a new instance of BaseModel"""
            self.assertEqual(output, test.getvalue().strip())

        # with patch("sys.stdout", new=SO()) as test:
        #  self.assertFalse(HB().onecmd("help emptyline"))
        # output = """nothing just pass"""
        # self.assertEqual(output, test.getvalue().strip())

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


class CreateTest(unittest.TestCase):
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

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "User.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "BaseModel.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "Amenity.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "Place.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "Review.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "City.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.create()"))
            self.assertLess(0, len(test.getvalue().strip()))
            test_cls = "State.{}".format(test.getvalue().strip())
            self.assertIn(test_cls, storage.all().keys())


class TestShow(unittest.TestCase):
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
            # instance id missing
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show User"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show Amenity"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show City"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show Place"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show BaseModel"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show Review"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("show State"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())

        # instance id missing with space
        # instance id missing
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.show()"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.show()"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.show()"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.show()"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.show"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.show()"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.show"))
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

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.show(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())


class UpdateTest(unittest.TestCase):
    def test_update(self):
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update"))
            output = "** class name missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update USER"))
            output = "** class doesn't exist **"
            self.assertEqual(output, test.getvalue().strip())
            # instance id missing
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update User"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update Amenity"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update City"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update Place"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update BaseModel"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update Review"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("update State"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())

        # instance id missing with dot
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.update"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())


class DestroyTest(unittest.TestCase):
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

            # instance id missing
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy User"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy Amenity"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy City"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy Place"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy BaseModel"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy Review"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("destroy State"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())

            # instance id missing with dot
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.destroy"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.destroy"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.destroy"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.destroy"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.destroy"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.destroy"))
            output = "** instance id missing **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.destroy"))
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
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())

        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.destroy(2e3)"))
            output = "** no instance found **"
            self.assertEqual(output, test.getvalue().strip())


class All_test(unittest.TestCase):
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
            self.assertFalse(HB().onecmd("Amenity.create()"))
            self.assertFalse(HB().onecmd("Amenity.all()"))
            self.assertIn("Amenity", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.create()"))
            self.assertFalse(HB().onecmd("all Amenity"))
            self.assertIn("Amenity", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.create()"))
            self.assertFalse(HB().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.create()"))
            self.assertFalse(HB().onecmd("all BaseModel"))
            self.assertIn("BaseModel", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.create()"))
            self.assertFalse(HB().onecmd("City.all()"))
            self.assertIn("City", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.create()"))
            self.assertFalse(HB().onecmd("all City"))
            self.assertIn("City", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.create()"))
            self.assertFalse(HB().onecmd("Place.all()"))
            self.assertIn("Place", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.create()"))
            self.assertFalse(HB().onecmd("all Place"))
            self.assertIn("Place", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.create()"))
            self.assertFalse(HB().onecmd("Review.all()"))
            self.assertIn("Review", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.create()"))
            self.assertFalse(HB().onecmd("all Review"))
            self.assertIn("Review", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.create()"))
            self.assertFalse(HB().onecmd("State.all()"))
            self.assertIn("State", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.create()"))
            self.assertFalse(HB().onecmd("all State"))
            self.assertIn("State", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.create()"))
            self.assertFalse(HB().onecmd("User.all()"))
            self.assertIn("User", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.create()"))
            self.assertFalse(HB().onecmd("all User"))
            self.assertIn("User", test.getvalue().strip())


class TestCount(unittest.TestCase):
    """for a count test"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "count")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

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

    def test_count(self):
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Amenity.count()"))
            self.assertEqual("1", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("BaseModel.count()"))
            self.assertEqual("1", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("City.count()"))
            self.assertEqual("1", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Place.count()"))
            self.assertEqual("1", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("Review.count()"))
            self.assertEqual("1", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("State.count()"))
            self.assertEqual("1", test.getvalue().strip())
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.create()"))
        with patch("sys.stdout", new=SO()) as test:
            self.assertFalse(HB().onecmd("User.count()"))
            self.assertEqual("1", test.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
