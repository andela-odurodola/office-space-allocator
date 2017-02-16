#!/usr/bin/python3
import room


class LivingSpace(Room):

    def __init__(self, arg, max_occupant, member):
        Room.__init__(self, arg)
        self.max_occupant = 4
        self.member = []
