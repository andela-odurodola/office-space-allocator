#!/usr/bin/python3
from models.room.room import Room


class Office(Room):

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_type = "OFFICE"
        self.max_occupants = 6
