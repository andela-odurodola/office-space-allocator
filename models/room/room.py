#!/usr/local/bin/python3


class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []

    def is_member(self, person):
        if person in self.occupants:
            raise ValueError("{} is already a member of room {}".format(person, self.room_name))

class Office(Room):
    # Inheriting from room class
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_type = "OFFICE"
        self.max_occupants = 6

    def check_availability(self):
        if len(self.occupants) == self.max_occupants:
            raise ValueError("{} is full".format(self.room_name))

    @classmethod
    def reallocate_person(cls, person, room, unallocated_officelist):
        room.occupants.append(person)
        if person.office_space_allocated:
            person.office_space_allocated.occupants.remove(person)
        else:
            unallocated_officelist.remove(person)

        person.office_space_allocated = room
        print("{0} has been reallocated to the office {1}".format(person, room.room_name))


class LivingSpace(Room):
    # Inheriting from room class
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_type = "LIVINGSPACE"
        self.max_occupants = 4

    def check_availability(self):
        if len(self.occupants) == self.max_occupants:
            raise ValueError("{} is full".format(self.room_name))

    @classmethod
    def check_livingspace_allowance(cls, person):
        if person.rank == "STAFF":
            raise ValueError("Staff {} aren't allowed livingspaces".format(person))
        elif person.wants_accomodation == "n":
            raise ValueError("Fellow {} didn't register for accomodation".format(person))

    @classmethod
    def reallocate_person(cls, person, room, unallocated_livinglist):
        LivingSpace.check_livingspace_allowance(person)

        room.occupants.append(person)
        if person.living_space_allocated:
            person.living_space_allocated.occupants.remove(person)
        else:
            unallocated_livinglist.remove(person)

        person.living_space_allocated = room
        print("{0} has been reallocated to the livingspace {1}".format(person, room.room_name))
