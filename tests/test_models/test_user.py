#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import os
from datetime import datetime
from time import sleep
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import re
import json


class TestUserInstantiation(unittest.TestCase):
    """Test Cases for the User class instantiation."""

    def setUp(self):
        """Sets up test methods."""
        self.reset_storage()

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attribe()["User"]
        user = User()
        for attr, attr_type in attributes.items():
            self.assertTrue(hasattr(user, attr))
            self.assertEqual(type(getattr(user, attr, None)), attr_type)


class TestUserMethods(unittest.TestCase):
    """Test Cases for the User class methods."""

    def test_save(self):
        """Tests the save method of User class."""
        user = User()
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method of User class."""
        user = User()
        user.id = "123456"
        dt = datetime.today()
        user.created_at = user.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_user_str_representation(self):
        """Tests the __str__ method of User class."""
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)


if __name__ == "__main__":
    unittest.main()

