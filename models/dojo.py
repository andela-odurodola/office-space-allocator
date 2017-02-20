from models.room.office_space import Office
from models.room.living_space import LivingSpace
from models.room.room import Room
from models.person.person import Person
from models.person.fellow import Fellow
from models.person.staff import Staff
import random


class Dojo(object):
    """ The Dojo class"""

    rooms = {}
    persons = {}

    def __init__(self):
        pass

    def create_room(self, arg):
        """ This function creates a new room """

        room_type = arg["<room_type>"]
        room_names = arg["<room_name>"]

        for room_name in room_names:
            if room_type.upper() == "OFFICE":
                new_space = Office(room_name)
                self.rooms[room_name] = new_space

            elif room_type.upper() == "LIVINGSPACE":
                new_space = LivingSpace(room_name)
                self.rooms[room_name] = new_space

            else:
                print("Invalid Room")

            Prefix = ("A" if room_type.upper() == "LIVINGSPACE" else "An")
            print("{} {} called {} has been successfully created".format
                  (Prefix, room_type, room_name))

    def add_person(self, arg):
        """ This function adds a person """
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        rank = (arg["<FELLOW/STAFF>"])
        wants_accomodation = (arg["<wants_accomodation>"] or "N")

        if rank.upper() == "STAFF":
            new_user = Staff(first_name, last_name)
            self.persons[first_name] = new_user

        elif rank.upper() == "FELLOW":
            new_user = Fellow(first_name, last_name,
                              wants_accomodation.upper())
            self.persons[first_name] = new_user

        else:
            print("Invalid Person")
            return

        print("{} {} {} has been successfully added".format
              (self.persons[first_name].rank, self.persons[first_name].first_name, self.persons[first_name].last_name))

        hi = self.assign_person(new_user)
        print(hi)

        # self.persons[first_name][
        #     "wants_accomodation"] = nwants_accomodation.upper()

        # print(self.persons[first_name].last_name)

    def assign_person(self, person):
        """ This function randomly assigns a person to a room """
        if person.wants_accomodation == "Y":
            for room_name, room in self.rooms.items():
                return((room_name))

            # first_name, room_type,room_name
            # Room = self.rooms.keys()
            # for name in self.persons:
            #     for j in self.persons[name]:
            #         for yes in self.persons[name][j]:
            #             if yes == "Y":

            # return ("{} has been allocated the {}".format(
            #     self.persons[name], random.choice(Room)))

        # Neil has been allocated the office Blue
