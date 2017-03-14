
import unittest
import sys

from models.dojo import Dojo


class TestPrintAllocation(unittest.TestCase):
    """It tests for the functionality print room."""

    allocation_office = "green\n------------------------------\n[DAMILOLA DURODOLA]"

    allocation_living = "blue"\
                        + "\n------------------------------\n"\
                        + "[KOYA GBOYE]"

    def setUp(self):

        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_print_allocations_for_office(self):
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
        allocate_file = {
            '--o': None
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_allocations(allocate_file)
        result = "\n".join(sys.stdout.getvalue().split("\n")[3:6])
        self.assertEqual(result, self.allocation_office)

    def test_print_allocations_for_livingspace(self):
        """."""
        room_detail = {
            '<room_type>': 'livingspace',
            '<room_name>': ['blue']
            }
        person_details = {
            '<first_name>': 'Koya',
            '<last_name>': 'Gboye',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }
        allocate_file = {
            '--o': None
        }

        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_allocations(allocate_file)
        result = "\n".join(sys.stdout.getvalue().split("\n")[4:7])

        self.assertEqual(result, self.allocation_living)

    def test_print_allocations_for_office_with_textinput(self):
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
        allocate_file = {
            '--o': 'office'
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_allocations(allocate_file)
        office_file = open('office.txt', 'r')
        result = office_file.read()
        office_file.close()

        self.assertEqual(result, self.allocation_office)

    def test_print_allocations_for_living_with_textinput(self):
        """."""
        room_detail = {
            '<room_type>': 'livingspace',
            '<room_name>': ['blue']
            }
        person_details = {
            '<first_name>': 'Koya',
            '<last_name>': 'Gboye',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }
        allocate_file = {
            '--o': 'livingg'
        }
        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_allocations(allocate_file)
        living_file = open('livingg.txt', 'r')
        result = living_file.read()
        living_file.close()

        self.assertEqual(result, self.allocation_living)
