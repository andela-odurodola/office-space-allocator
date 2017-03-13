import unittest
import sys

from models.dojo import Dojo


class TestLoadPeople(unittest.TestCase):
    """It tests for the functionality of loading people from a text file."""

    def setUp(self):
        """sets."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def tearDown(self):
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_load_staff_successfully(self):
        """It tests for staff."""
        staff_details = {
            '<text_file>': 'load_staff.txt'
        }
        room_details = {
            '<room_type>': 'office',
            '<room_name>': ['red']
        }

        self.dojo.create_room(room_details)
        staff_file = open('load_staff.txt', 'r')
        staff_file.read()
        staff_file.close()
        self.dojo.load_people(staff_details)

        self.assertEqual(len(self.dojo.office_rooms), 1)

    def test_load_fellow_successfully(self):
        """It tests for fellow."""
        fellow_details = {
            '<text_file>': 'load_staff.txt'
        }
        room_details = {
            '<room_type>': 'livingspace',
            '<room_name>': ['blue']
        }

        self.dojo.create_room(room_details)
        staff_file = open('load_fellow.txt', 'r')
        staff_file.read()
        staff_file.close()
        self.dojo.load_people(fellow_details)

        self.assertEqual(len(self.dojo.living_rooms), 1)
