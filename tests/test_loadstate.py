#!/usr/local/bin/python3
import sys
import os
import unittest

from database_model.database_states import DatabaseManager, OfficeRooms, LivingRooms, Persons
from models.dojo import Dojo


class TestLoadState(unittest.TestCase):

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_if_file_exist(self):
        with self.assertRaises(Exception) as result:
            self.dojo.load_state('te.db')

        self.assertEqual(str(result.exception),
                         "File does not exist.")
