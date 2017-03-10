#!/usr/local/bin/python3
from models.room.room import Room


class Office(Room):
    """subclass inheriting from room class."""

    def __init__(self, room_name):
        """Constructor function for office class."""
        super().__init__(room_name)
        self.room_type = "OFFICE"
        self.max_occupants = 6
