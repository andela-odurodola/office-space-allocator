#!/usr/local/bin/python3
import random
import string



class Person(object):

    def __init__(self, first_name, last_name, wants_accomodation="n"):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.wants_accomodation = wants_accomodation
        self.office_space_allocated = None
        self.living_space_allocated = None

    def __repr__(self):
        # It prints a representation of the person object
        return "{0} {1}".format(self.first_name, self.last_name)


class Fellow(Person):

    def __init__(self, first_name, last_name, wants_accomodation):
        super().__init__(first_name, last_name, wants_accomodation)
        self.identifier = self.get_fellow_identifier
        self.rank = "FELLOW"

    def get_fellow_identifier(self):
        fellow_id = 'F'.join([random.choice(string.ascii_letters + string.digits) for n in xrange(4)])
        return fellow_id

class Staff(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "n")
        self.identifier = self.get_staff_identifier
        self.rank = "STAFF"

    def get_staff_identifier(self):
        staff_id = 'S'.join([random.choice(string.ascii_letters + string.digits) for n in xrange(4)])
        return staff_id
