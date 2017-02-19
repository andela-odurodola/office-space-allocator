#!/usr/bin/python3
from models.room.room import Room


class LivingSpace(Room):

    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_type = "LIVINGSPACE"
        self.max_occupants = 4
