import sys
import unittest

from models.dojo import Dojo


class TestCreateRoom(unittest.TestCase):
    # It tests functionalities for room creation

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_create_room_office_successfully(self):
        # It tests that room type office is created
        initial_room_count = len(self.dojo.office_rooms)
        self.dojo.create_room('office', ['blue', 'red'])
        new_room_count = len(self.dojo.office_rooms)

        self.assertEqual(new_room_count - initial_room_count, 2)

    def test_invalid_room_type(self):
        # It tests when an invalid room type is entered
        with self.assertRaises(ValueError) as result:
            self.dojo.create_room('Cafeteria', ['white'])
        self.assertEqual(str(result.exception),
                         "Invalid Room Type.Must be office or living")

    def test_if_new_room_name_already_exist(self):
        self.dojo.create_room('office', ['red'])
        self.dojo.create_room('office', ['blue', 'red'])
        result = sys.stdout.getvalue().split("\n")[2]
        self.assertEqual(result, "The room red exists. Try again")

    def test_create_room_living_successfully(self):
        # It tests that room type living is created
        initial_room_count = len(self.dojo.living_rooms)
        self.dojo.create_room('livingspace', ['black'])
        new_room_count = len(self.dojo.living_rooms)

        self.assertEqual(new_room_count - initial_room_count, 1)
