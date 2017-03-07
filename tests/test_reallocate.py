import unittest
import sys

from models.dojo import Dojo


class TestReallocatePerson(unittest.TestCase):
    """It tests for the functionality Reallocate Person to a new room."""

    def setUp(self):
        """sets."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_for_invalid_roomname_and_personid(self):
        """It tests for invalid input."""
        reallocate_details = {
            '<person_identifier>': 'S3',
            '<new_room_name>': 'pink'
        }
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
        self.dojo.reallocate_person(reallocate_details)
        result = sys.stdout.getvalue().split("\n")[3]
        self.assertEqual(result,
                         "Person S3 does not exist or room name is invalid")

    # def test_if_person_is_already_a_member(self):
    #     """It tests for membership in a room."""
    #     reallocate_details = {
    #         '<person_identifier>': 'S1',
    #         '<new_room_name>': 'green'
    #     }
    #     room_detail = {
    #         '<room_type>': 'office',
    #         '<room_name>': ['green']
    #         }
    #     person_details = {
    #         '<first_name>': 'Koya',
    #         '<last_name>': 'Gboye',
    #         '<FELLOW/STAFF>': 'staff',
    #         '<wants_accomodation>': ''
    #     }
    #     self.dojo.create_room(room_detail)
    #     self.dojo.add_person(person_details)
    #     self.dojo.reallocate_person(reallocate_details)
    #     result = sys.stdout.getvalue().split("\n")
    #     self.assertEqual(result,
    #                      "Person S1 is already a member of room green")
    #
    # def test_reallocate_staff(self):
    #     """It tests for reallocation of staff to a new room."""
    #     reallocate_details = {
    #         '<person_identifier>': 'S1',
    #         '<new_room_name>': 'blue'
    #     }
    #     room_detail = {
    #         '<room_type>': 'office',
    #         '<room_name>': ['green', 'blue']
    #         }
    #     person_details = {
    #         '<first_name>': 'Abdul',
    #         '<last_name>': 'Mumyeen',
    #         '<FELLOW/STAFF>': 'staff',
    #         '<wants_accomodation>': ''
    #     }
    #
    #     self.dojo.create_room(room_detail)
    #     self.dojo.add_person(person_details)
    #     self.dojo.reallocate_person(reallocate_details)
    #     result = sys.stdout.getvalue().split("\n")
    #     self.assertEqual(result,
    #                      "identifier S1 has been reallocated to the office blue")
    #
    # def test_reallocate_fellow(self):
    #     """It tests for reallocation of staff to a new room."""
    #     reallocate_details = {
    #         '<person_identifier>': 'F1',
    #         '<new_room_name>': 'blue'
    #     }
    #     room_detail = {
    #         '<room_type>': 'livingspace',
    #         '<room_name>': ['green', 'blue']
    #         }
    #     person_details = {
    #         '<first_name>': 'Bolaji',
    #         '<last_name>': 'Jide',
    #         '<FELLOW/STAFF>': 'fellow',
    #         '<wants_accomodation>': 'y'
    #     }
    #
    #     self.dojo.create_room(room_detail)
    #     self.dojo.add_person(person_details)
    #     self.dojo.reallocate_person(reallocate_details)
    #     result = sys.stdout.getvalue().split("\n")
    #     self.assertEqual(result,
    #                      "identifier F1 has been reallocated to the office blue")
