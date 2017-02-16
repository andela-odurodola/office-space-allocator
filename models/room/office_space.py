#!/usr/bin/python3
import room


class Office(Room):

    def __init__(self, arg, max_occupant, member):
        Room.__init__(self, arg)
        self.max_occupant = 6
        self.member = []
