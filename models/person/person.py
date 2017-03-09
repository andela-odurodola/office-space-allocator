#!/usr/bin/python3
class Person(object):
    """The person class."""

    id = 0

    def __init__(self, first_name, last_name, wants_accomodation="N"):
        """Constructor function for person class."""
        type(self).id += 1
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.full_name = first_name + " " + last_name
        self.wants_accomodation = wants_accomodation
        self.office_space_allocated = ""
        self.living_space_allocated = ""

    def __repr__(self):
        """It prints a representation of the person object."""
        return "{0} {1}".format(self.first_name, self.last_name)
