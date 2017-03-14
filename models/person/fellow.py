#!/usr/local/bin/python3
from models.person.person import Person


class Fellow(Person):
    """Subclass inheriting from person class."""

    def __init__(self, first_name, last_name, wants_accomodation):
        """Constructor function for fellow class."""
        super().__init__(first_name, last_name, wants_accomodation)
        self.rank = "FELLOW"
