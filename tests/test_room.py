"""Testing for CreateRoom."""
import unittest

from models.dojo import Dojo


class TestCreateRoom(unittest.TestCase):
    """It tests functionalities for room creation."""

    def setUp(self):
        """Set."""
        self.dojo = Dojo()
        self.dojo.office_rooms = {}
        self.dojo.living_rooms = {}
        self.dojo.persons = {}

    def test_create_room_office_successfully(self):
        """It tests that room type office is created."""
        test_rooms = ['blue', 'red', 'pink']
        room_details = {
            '<room_type>': 'office',
            '<room_name>': test_rooms
        }

        self.dojo.create_room(room_details)

        num_test_rooms = len(test_rooms)
        num_dojo_offices = len(self.dojo.office_rooms)

        self.assertEqual(num_dojo_offices, num_test_rooms)

    def test_invalid_room_type(self):
        """It tests when an invalid room type is entered."""
        test_rooms = ['blue', 'red', 'white']
        room_details = {
            '<room_type>': 'Cafeteria',
            '<room_name>': test_rooms
        }

        with self.assertRaises(ValueError) as result:
            self.dojo.create_room(room_details)
        self.assertEqual(str(result.exception),
                         "Invalid Room Type.Must be office or living")

    def test_for_invalid_room_name(self):
        """It tests when an invalid room name is entered."""
        room_details = {
            '<room_type>': 'office',
            '<room_name>': ['office', 'livingspace']
        }

        with self.assertRaises(ValueError) as result:
            self.dojo.create_room(room_details)
        self.assertEqual(str(result.exception),
                         "This is not a valid room name")

    def test_create_room_living(self):
        """It tests that room type living is created."""
        test_room = ['green']
        room_details = {
            '<room_type>': 'Livingspace',
            '<room_name>': test_room
        }

        self.dojo.create_room(room_details)

        num_test_rooms = len(test_room)
        num_dojo_living = len(self.dojo.living_rooms)

        self.assertEqual(num_dojo_living, num_test_rooms)
