import unittest
import sys

from models.dojo import Dojo


class TestPrintAllocation(unittest.TestCase):
    # It tests for the functionality print allocations for rooms

    allocation_office = "diamond\n------------------------------\n[NORA ROBERT]"

    allocation_living = "sapphire"\
                        + "\n------------------------------\n"\
                        + "[KOYA GBOYE]\n"

    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        Dojo.office_rooms = []
        Dojo.living_rooms = []
        Dojo.persons = []
        Dojo.unallocated_officelist = []
        Dojo.unallocated_livinglist = []

    def test_print_allocations_to_screen(self):
        self.dojo.create_room('office', ['diamond'])
        self.dojo.add_person('Nora', 'Robert', 'fellow', '')
        self.dojo.print_allocations(None)
        result = "\n".join(sys.stdout.getvalue().split("\n")[3:6])

        self.assertEqual(result, self.allocation_office)

    def test_print_allocations_with_textinput(self):
        self.dojo.create_room('livingspace', ['sapphire'])
        self.dojo.add_person('Koya', 'Gboye', 'fellow', 'y')
        self.dojo.print_allocations('liv')
        with open('liv.txt', 'r') as result:
            result_file = result.read()

        self.assertEqual(result_file, self.allocation_living)
