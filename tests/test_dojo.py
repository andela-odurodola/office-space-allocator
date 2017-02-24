import unittest
from models.dojo import Dojo


class Test_create_room(unittest.TestCase):

    def test_create_room_successfully(self):
        my_class_instance = MyClass()
        initial_room_count = len(my_class_instance.all_rooms)
        blue_office = my_class.create_room(“Blue”, “office”)
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
