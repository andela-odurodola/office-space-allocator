
import unittest
import sys

from models.dojo import Dojo


class TestPrintRoom(unittest.TestCase):
    """It tests for the functionality print room."""

    def setUp(self):
        """sets."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_that_it_prints_occupants_officeroom(self):
        """It tests."""
        room_detail = {
            '<room_type>': 'office',
            '<room_name>': ['green']
        }
        room = {
            '<room_name>': 'green'
        }
        person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_room(room)
        result = sys.stdout.getvalue().split("\n")[-2]

        self.assertEqual(result, 'Office room occupants --- [DAMILOLA DURODOLA]')

    def test_that_it_prints_occupants_living_room(self):
        """It tests."""
        room_detail = {
            '<room_type>': 'livingspace',
            '<room_name>': ['pink']
        }
        room = {
            '<room_name>': 'pink'
        }
        person_details = {
            '<first_name>': 'Bolaji',
            '<last_name>': 'Adedeji',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_room(room)
        result = sys.stdout.getvalue().split("\n")[-2]

        self.assertEqual(result, 'Living room occupants --- [BOLAJI ADEDEJI]')

    def test_for_invalid_room(self):
        """It tests."""
        room_detail = {
            '<room_type>': 'office',
            '<room_name>': ['baboon']
        }
        room = {
            '<room_name>': 'violet'
        }
        person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        result = self.dojo.print_room(room)

        self.assertRaises(Exception, result, room)

    def test_for_empty_office_room(self):
        """It tests."""
        room_detail = {
            '<room_type>': 'office',
            '<room_name>': ['red']
        }
        room = {
            '<room_name>': 'red'
        }

        self.dojo.create_room(room_detail)
        result = self.dojo.print_room(room)

        self.assertRaises(Exception, result, room)

    def test_for_empty_living_room(self):
        """It tests."""
        room_detail = {
            '<room_type>': 'livingspace',
            '<room_name>': ['blue']
        }
        room = {
            '<room_name>': 'blue'
        }

        self.dojo.create_room(room_detail)
        result = self.dojo.print_room(room)

        self.assertRaises(Exception, result, room)
