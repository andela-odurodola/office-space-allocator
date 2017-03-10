#!/usr/local/bin/python3
import sys
import os
import unittest

from database_model.database_states import DatabaseManager, OfficeRooms, LivingRooms, Persons
from models.dojo import Dojo


class TestLoadState(unittest.TestCase):
    """It tests for data persistence."""

    def setUp(self):
        """It runs the method prior to each test."""
        self.dojo = Dojo()
        self.data = {'<sqlite_database>': 'testing.db'}
        self.invaliddata = {'<sqlite_database>': 'te.db'}

    def test_if_file_exist(self):
        with self.assertRaises(Exception) as result:
            self.dojo.load_state(self.invaliddata)
            
        self.assertEqual(str(result.exception),
                         "File does not exist.")

    def test_for_load_database_successfully(self):
        self.dojo.load_state(self.data)
        result = sys.stdout.getvalue().split("\n")[2]
        self.assertEqual("{'S1': PERCI NJIRA, 'F1': DAMI DURO}", result)
