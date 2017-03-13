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
        self.invaliddata = {'<sqlite_database>': 'te.db'}

    def tearDown(self):
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_if_file_exist(self):
        with self.assertRaises(Exception) as result:
            self.dojo.load_state(self.invaliddata)

        self.assertEqual(str(result.exception),
                         "File does not exist.")
