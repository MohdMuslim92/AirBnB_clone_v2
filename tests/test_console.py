#!/usr/bin/python3
"""A unit test module for the console"""

import unittest
import json
import console
import pep8
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """testing console.py"""

    def test_prompt_string(self):
        """ To test the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_pep8e(self):
        """ To test pep8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors")

    def test_create(self):
        """Test that create"""
        x = self.create()
        x.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):
        """Testing the error for class name missing"""
        x = self.create()
        x.onecmd("create")
        y = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)
