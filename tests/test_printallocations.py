
import unittest

from models.dojo import Dojo


class TestPrintRoom(unittest.TestCase):
    """It tests for the functionality print room."""

    allocation_txt = "green\n" +\
                    "------------------------------\n" +\
                    "[DAMILOLA DURODOLA]\n"

    def setUp(self):
        """sets."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_print_allocations(self):
        """."""
        room_detail = {
            '<room_type>': 'office',
            '<room_name>': ['green']
            }
        person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_allocations(self)
        print(self.allocation_txt)
        self.assertEqual()
