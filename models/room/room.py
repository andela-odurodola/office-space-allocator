#!/usr/local/bin/python3


class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []


class Office(Room):
    # Inheriting from room class

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_type = "OFFICE"
        self.max_occupants = 6


class LivingSpace(Room):
    # Inheriting from room class

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_type = "LIVINGSPACE"
        self.max_occupants = 4
