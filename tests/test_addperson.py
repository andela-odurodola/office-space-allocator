#!/usr/local/bin/python3
import unittest

from models.dojo import Dojo


class TestAddPerson(unittest.TestCase):
    # It tests functionalities for adding and assigning people to room

    def setUp(self):
        # It runs the method prior to each test
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo.office_rooms = []
        self.dojo.living_rooms = []
        self.dojo.persons = []

    def test_add_person_staff_succesfully(self):
        # It tests if person who is a staff is created successfully
        self.dojo.add_person('Damilola', 'Durodola', 'staff', '')
        person_name = [str(person) for person in self.dojo.persons]

        self.assertIn('DAMILOLA DURODOLA', person_name)

    def test_add_person_fellow_with_no_accomodation(self):
        # It tests if person who is a fellow is created successfully
        self.dojo.add_person('Fola', 'Woju', 'fellow', '')
        person_name = [str(person) for person in self.dojo.persons]

        self.assertIn('FOLA WOJU', person_name)

    def test_if_person_is_added_to_room(self):
        # It tests whether a person is added to a room
        self.dojo.create_room('office', ['pink'])
        self.dojo.add_person('Tolu', 'Ade', 'fellow', '')

        for room in self.dojo.office_rooms:
            room_occupied = room.occupants

        self.assertIn('TOLU ADE', str(room_occupied))

    def test_for_fellow_with_wants_accomodation(self):
        # It tests whether a person is added to a room
        self.dojo.create_room('livingspace', ['green'])
        self.dojo.add_person('Jide', 'Ade', 'Fellow', 'y')

        for room in self.dojo.living_rooms:
            room_occupied = room.occupants

        self.assertIn('JIDE ADE', str(room_occupied))

    def test_for_invalid_person_type(self):
        # It tests whether a person is added to a room
        with self.assertRaises(Exception) as result:
            self.dojo.add_person('Sola', 'Sanu', 'caterer', '')
        self.assertEqual(str(result.exception),
                         "Person can only be a fellow or staff")
