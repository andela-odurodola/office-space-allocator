#!/usr/bin/python3
from models.person.person import Person


class Staff(Person):
    """subclass inheriting from perso class."""

    def __init__(self, first_name, last_name):
        """Constructor funtion for staff class."""
        super().__init__(first_name, last_name, "N")
        self.rank = "STAFF"
