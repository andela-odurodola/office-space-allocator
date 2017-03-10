#!/usr/local/bin/python3


class Room(object):
    """It defines the room class."""

    def __init__(self, room_name):
        """Constructor for room class."""
        self.room_name = room_name
        self.occupants = []
