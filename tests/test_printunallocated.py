
import unittest
import sys

from models.dojo import Dojo


class TestPrintUnallocated(unittest.TestCase):
    """It tests for the functionality print unallocated person."""

    def setUp(self):
        """sets."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_print_unallocated_without_acccomodation(self):
        """."""
        person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        allocate_file = {
            '--o': None
        }

        self.dojo.add_person(person_details)
        self.dojo.print_unallocated(allocate_file)
        result = sys.stdout.getvalue().strip().split("\n")[2]

        self.assertEqual(result, "Unallocated persons ----DAMILOLA DURODOLA")

    def test_print_unallocated_with_acccomodation(self):
        """."""
        room_detail = {
                '<room_type>': 'office',
                '<room_name>': ['blue']
                }
        person_details = {
            '<first_name>': 'ladi',
            '<last_name>': 'Adediran',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }
        allocate_file = {
            '--o': None
        }

        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_unallocated(allocate_file)
        result = sys.stdout.getvalue().strip().split("\n")[-1]

        self.assertEqual(result, "Unallocated persons ----LADI ADEDIRAN")

    def test_print_unallocated_without_acccomodation_with_file(self):
        """."""
        person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        allocate_file = {
            '--o': 'staff'
        }

        self.dojo.add_person(person_details)
        self.dojo.print_unallocated(allocate_file)
        unallocated_staff = open('staff.txt', 'r')
        result = unallocated_staff.read()
        unallocated_staff.close()

        self.assertEqual(result, "Unallocated persons ----DAMILOLA DURODOLA")

    def test_print_unallocated_with_acccomodation_with_file(self):
        """It test for print allocated with a filename."""
        room_detail = {
                '<room_type>': 'office',
                '<room_name>': ['blue']
                }
        person_details = {
            '<first_name>': 'ladi',
            '<last_name>': 'Adediran',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }
        allocate_file = {
            '--o': 'fellow'
        }

        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)
        self.dojo.print_unallocated(allocate_file)
        unallocated_fellow = open('fellow.txt', 'r')
        result = unallocated_fellow.read()
        unallocated_fellow.close()

        self.assertEqual(result, "Unallocated persons ----LADI ADEDIRAN")

    def test_invalid_input_for_print_unallocated(self):
        """It tests when everyone has been allocated."""
        room_detail = {
                '<room_type>': 'office',
                '<room_name>': ['gren']
                }
        person_details = {
            '<first_name>': 'Ichiat',
            '<last_name>': 'Ikikin',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }
        allocate_file = {
            '--o': None
        }

        self.dojo.create_room(room_detail)
        self.dojo.add_person(person_details)

        with self.assertRaises(Exception) as result:
            self.dojo.print_unallocated(allocate_file)
        self.assertEqual(str(result.exception),
                         "Everyone has been allocated")
