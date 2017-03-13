#!/usr/local/bin/python3
import os
import unittest

from database_model.database_states import DatabaseManager, Persons
from models.dojo import Dojo


class TestSaveState(unittest.TestCase):
    """It tests for data persistence."""

    def setUp(self):
        """It runs the method prior to each test."""
        self.dojo = Dojo()
        self.person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        self.data = {'--db': None}

    def tearDown(self):
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_for_database(self):

        self.dojo.add_person(self.person_details)
        self.dojo.save_state(self.data)

        database = DatabaseManager('database_model/test.db')
        database_session = database.Session()

        for row in database_session.query(Persons):
            saved_data = row.person_info
            database_id = list(saved_data)[0]
            self.assertEqual(database_id, 'S1')
