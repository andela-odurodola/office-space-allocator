
import unittest
import sys

from models.dojo import Dojo


class TestPrintUnallocated(unittest.TestCase):
    # It tests for the functionality print unallocated person
    unallocated_text = 'Unallocated persons for office rooms----[LADI JOSE]\n'\
                        + 'Unallocated persons for living rooms----[LADI JOSE]'
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_print_unallocated_to_screen(self):
        self.dojo.add_person('Ladi', 'Jose', 'fellow', 'y')
        self.dojo.print_unallocated(None)
        result = '\n'.join(sys.stdout.getvalue().split("\n")[3:5])

        self.assertEqual(result, self.unallocated_text)

    def test_print_unallocated_to_text_file(self):
        self.dojo.add_person('Ladi', 'Jose', 'fellow', 'y')
        self.dojo.print_unallocated('loc')
        with open('loc.txt', 'r') as output:
            output_file = output.read()

        self.assertEqual(output_file, self.unallocated_text)

    def test_when_everyone_is_allocated(self):
        self.dojo.create_room('office', ['osborne'])
        self.dojo.add_person('Ichiat', 'Ikikin', 'staff', '')
        self.dojo.print_unallocated(None)
        result = sys.stdout.getvalue().split("\n")[3]

        self.assertEqual(result,
                         "Everyone has been allocated")
