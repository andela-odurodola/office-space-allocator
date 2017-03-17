
import unittest
import sys

from models.dojo import Dojo


class TestPrintRoom(unittest.TestCase):
    # It tests for the functionality print room

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_that_it_prints_occupants_officeroom(self):
        self.dojo.create_room('office', ['purple'])
        self.dojo.add_person('Bola', 'Kola', 'staff', '')
        self.dojo.print_room('purple')
        result = sys.stdout.getvalue().split("\n")[-2]

        self.assertEqual(result, 'Room occupants --- [BOLA KOLA]')

    def test_that_it_prints_occupants_living_room(self):
        self.dojo.create_room('livingspace', ['yellow'])
        self.dojo.add_person('Bolaji', 'Adedeji', 'fellow', 'y')
        self.dojo.print_room('yellow')
        result = sys.stdout.getvalue().split("\n")[4]

        self.assertEqual(result, 'Room occupants --- [BOLAJI ADEDEJI]')

    def test_for_invalid_room(self):
        with self.assertRaises(ValueError) as result:
            self.dojo.print_room('violet')
        self.assertEqual(str(result.exception),
                         "The room violet has not been created")

    def test_for_empty_office_room(self):
        self.dojo.create_room('office', ['maroon'])
        self.dojo.print_room('maroon')
        result = sys.stdout.getvalue().split("\n")[1]
        self.assertEqual(result,
                         "The room maroon is empty")

    def test_for_empty_living_room(self):
        self.dojo.create_room('livingspace', ['wine'])
        self.dojo.print_room('wine')
        result = sys.stdout.getvalue().split("\n")[1]

        self.assertEqual(result,
                         "The room wine is empty")
