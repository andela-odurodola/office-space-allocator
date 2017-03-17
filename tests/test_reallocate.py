import unittest
import sys

from models.dojo import Dojo


class TestReallocatePerson(unittest.TestCase):
    # It tests for the functionality Reallocate Person to a new room

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_for_invalid_roomname_and_personid(self):
        self.dojo.create_room('office', ['sapphire'])
        self.dojo.add_person('Liz', 'Gowon', 'staff', '')
        self.dojo.reallocate_person('aSwSed', 'grey')
        result = sys.stdout.getvalue().split("\n")[3]
        self.assertEqual(result,
                         "Person with the id aSwSed or room grey does not exist")

    def test_if_person_is_already_a_member(self):
        self.dojo.create_room('office', ['grey'])
        self.dojo.add_person('Ladi', 'Toni', 'fellow', '')
        person_id = Dojo.persons[0].identifier
        self.dojo.reallocate_person(person_id, 'grey')
        result = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(result,
                         "LADI TONI is already a member of room grey")

    def test_reallocate_staff(self):
        self.dojo.create_room('office', ['potash'])
        self.dojo.add_person('Abdul', 'Mumyeen', 'staff', '')
        self.dojo.create_room('office', ['aqua'])
        person_id = Dojo.persons[0].identifier
        self.dojo.reallocate_person(person_id, 'aqua')
        result = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(result,
                         "ABDUL MUMYEEN has been reallocated to the office aqua")

    def test_reallocate_fellow(self):
        self.dojo.create_room('livingspace', ['lemon'])
        self.dojo.add_person('Ade', 'Bola', 'fellow', 'y')
        self.dojo.create_room('livingspace', ['brown'])
        person_id = Dojo.persons[0].identifier
        self.dojo.reallocate_person(person_id, 'brown')
        result = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(result,
                         "ADE BOLA has been reallocated to the livingspace brown")
