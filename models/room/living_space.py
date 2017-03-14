#!/usr/local/bin/python3
from models.room.room import Room


class LivingSpace(Room):
    """subclass inheriting from room class."""

    def __init__(self, room_name):
        """Constructor for livingspace."""
        super().__init__(room_name)
        self.room_type = "LIVINGSPACE"
        self.max_occupants = 4
