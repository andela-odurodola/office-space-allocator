
import unittest

from models.dojo import Dojo
from models.person.fellow import Fellow
from models.person.person import Person
from models.person.staff import Staff


class TestAddPerson(unittest.TestCase):
    """It tests functionalities for adding and assigning people to room."""

    def setUp(self):
        """It runs the method prior to each test."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_add_person_staff_succesfully(self):
        """It tests if person who is a staff is created successfully."""
        person_details = {
            '<first_name>': 'Damilola',
            '<last_name>': 'Durodola',
            '<FELLOW/STAFF>': 'staff',
            '<wants_accomodation>': ''
        }

        self.dojo.add_person(person_details)
        list_of_person = [
            person_info.full_name for person_id,
            person_info in self.dojo.persons.items()]

        self.assertTrue('Damilola Durodola' in list_of_person)

    def test_add_person_fellow_succesfully(self):
        """It tests if person who is a fellow is created successfully."""
        person_details = {
            '<first_name>': 'Tolu',
            '<last_name>': 'Ade',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }

        self.dojo.add_person(person_details)
        list_of_person = [
            person_info.full_name for person_info
            in self.dojo.persons.values()]

        self.assertTrue('Tolu Ade' in list_of_person)

    def test_for_valid_id(self):
        """It checks for the type of person."""
        room_details = {
            '<room_type>': 'office',
            '<room_name>': ['pink']
        }
        person_details = {
            '<first_name>': 'Tolu',
            '<last_name>': 'Ade',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }

        self.dojo.create_room(room_details)
        self.dojo.add_person(person_details)
        list_of_person = [
            person_id for person_id,
            person_info in self.dojo.persons.items()]

        self.assertTrue('F3' in list_of_person)

    def test_if_person_is_added_to_room(self):
        """It tests whether a person is added to a room."""
        room_details = {
            '<room_type>': 'office',
            '<room_name>': ['pink']
        }

        person_details = {
            '<first_name>': 'Tolu',
            '<last_name>': 'Ade',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': ''
        }

        self.dojo.create_room(room_details)
        self.dojo.add_person(person_details)
        for room_info in self.dojo.office_rooms.values():
            occupant = len(room_info.occupants)

        self.assertEqual(occupant, 1)

    def test_for_fellow_with_wants_accomodation(self):
        """It tests whether a person is added to a room."""
        room_details = {
            '<room_type>': 'livingspace',
            '<room_name>': ['green']
        }
        person_details = {
            '<first_name>': 'Jide',
            '<last_name>': 'Ade',
            '<FELLOW/STAFF>': 'fellow',
            '<wants_accomodation>': 'y'
        }
        self.dojo.create_room(room_details)
        self.dojo.add_person(person_details)
        for room_info in self.dojo.living_rooms.values():
            occupant = len(room_info.occupants)

        self.assertEqual(occupant, 1)

    def test_for_invalid_person_type(self):
        """It tests whether a person is added to a room."""
        person_details = {
            '<first_name>': 'Jide',
            '<last_name>': 'Ade',
            '<FELLOW/STAFF>': 'caterer',
            '<wants_accomodation>': ''
        }

        with self.assertRaises(Exception) as result:
            self.dojo.add_person(person_details)
        self.assertEqual(str(result.exception),
                         "Person can only be a fellow or staff")
