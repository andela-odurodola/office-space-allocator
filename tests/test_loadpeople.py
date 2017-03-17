import unittest
import sys

from models.dojo import Dojo


class TestLoadPeople(unittest.TestCase):
    # It tests for the functionality of loading people from a text file

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []

    def test_load_staff_successfully(self):
        # It tests for staff
        self.dojo.create_room('office', ['silver'])
        with open('load_staff.txt', 'r') as staff_file:
            staff_file.read()

        self.dojo.load_people('load_staff.txt')

        self.assertEqual(len(self.dojo.office_rooms), 1)

    def test_load_fellow_successfully(self):
        # It tests for fellow
        self.dojo.create_room('livingspace', ['gold'])
        with open('load_fellow.txt', 'r') as fellow_file:
            fellow_file.read()

        self.dojo.load_people('load_fellow.txt')

        self.assertEqual(len(self.dojo.living_rooms), 1)
