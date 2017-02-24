from models.room.office_space import Office
from models.room.living_space import LivingSpace
from models.room.room import Room
from models.person.person import Person
from models.person.fellow import Fellow
from models.person.staff import Staff
import random
import pdb


class Dojo(object):
    """ The Dojo class"""

    office_room = {}
    living_room = {}
    persons = {}

    def __init__(self):
        pass

    def create_room(self, arg):
        """ This function creates a new room """

        room_type = arg["<room_type>"]
        room_names = arg["<room_name>"]

        for room_name in room_names:
            if room_type.upper() == "OFFICE":
                self.office_room[room_name] = Office(room_name)

            elif room_type.upper() == "LIVINGSPACE":
                self.living_room[room_name] = LivingSpace(room_name)

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

        # print(self.persons[first_name].id)
        print("{} {} {} has been successfully added".format
              (self.persons[first_name].rank, self.persons[first_name].first_name, self.persons[first_name].last_name))

        self.assign_person(new_user)

    @staticmethod
    def get_available_room_spaces(room_spaces):
        available_room_spaces = []
        for room, room_info in room_spaces.items():
            if (len(room_info.occupants) < room_info.max_occupants):
                available_room_spaces.append(room_info)
        return available_room_spaces

    def assign_person(self, person):
        """ This function randomly assigns a person to a room """

        available_office_spaces = self.get_available_room_spaces(
            self.office_room)
        if available_office_spaces == []:
            print("There is currently no office space")
        else:
            # pdb.set_trace()
            assigned_office_space = random.choice(available_office_spaces)
            assigned_office_space.occupants.append(person)
            print ("{0} has been allocated the office {1}".format(
                person.first_name, assigned_office_space.room_name))

        if person.wants_accomodation.upper() == "Y":
            available_living_spaces = self.get_available_room_spaces(
                self.living_room)
            if available_living_spaces == []:
                print("Room is full")
            else:
                assigned_living_space = random.choice(available_living_spaces)
                assigned_living_space.occupants.append(person)
                print ("{0} has been allocated the livingspace {1}".format(
                    person.first_name, assigned_living_space.room_name))
