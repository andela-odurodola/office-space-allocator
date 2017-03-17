#!/usr/local/bin/python3
import os
import unittest

from database_model.database_states import DatabaseManager, Persons
from models.dojo import Dojo


class TestSaveState(unittest.TestCase):
    # It tests for data persistence

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_for_database(self):
        self.dojo.add_person('Laye', 'Tomi', 'Staff', '')
        self.dojo.save_state(None)

        database = DatabaseManager('database_model/room.db')
        database_session = database.session()

        for row in database_session.query(Persons):
            saved_data = row.person_info
            database_id = list(saved_data)[0]
            self.assertEqual(database_id, 'S1')
        os.remove('database_model/room.db')
