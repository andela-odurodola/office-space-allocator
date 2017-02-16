from models import room
from models import person


class Dojo(object):
    """ The Dojo class"""

    def __init__(self):
        self.rooms = []
        self.persons = []

    def create_room(self, arg):
        """ This function creates a new room """
        room_type = arg["<room_type>"]
        room_names = arg["<room_name>"]

        for room_name in room_names:
            self.rooms.append(room_name)
            prefix = "A" if room_type == "livingspace" else "An"
            print("%s %s called %s has been successfully created" %
                  (prefix,room_type, room_name))
        print(self.rooms, "....")       

    def add_person(self, arg):
        """ This function adds a person """
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        rank = (arg["<FELLOW/STAFF>"])
        wants_accomodation = arg["<wants_accomodation>"]

        if rank == 'FELLOW':
            print("%s %s %s has been successfully added" %
                  (self.rank, self.first_name, self.last_name))
        elif self.rank == "STAFF":
            print("%s %s %s has been successfully added" %
                  (self.rank, self.first_name, self.last_name))
        else:
            print("Invalid Person")
        # print(type(self.rank))

        # print("Staff Neil Armstrong has been successfully added")
        # Neil has been allocated the office Blue
