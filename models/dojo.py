import random

from models.room.office_space import Office
from models.room.living_space import LivingSpace
from models.person.fellow import Fellow
from models.person.staff import Staff


class Dojo(object):
    """The Dojo class."""

    office_rooms = {}
    living_rooms = {}
    persons = {}
    divider = ("\n{}\n".format("-" * 30))

    def __init__(self):
        pass

    def create_room(self, arg):
        """The function creates a new room."""
        room_type = arg["<room_type>"]
        room_names = arg["<room_name>"]
        for room_name in room_names:
            if room_name == ('office' or 'livingspace'):
                raise Exception("This is not a valid room name")
            else:
                if room_type.upper() == "OFFICE":
                    self.office_rooms[room_name] = Office(room_name)

                elif room_type.upper() == "LIVINGSPACE":
                    self.living_rooms[room_name] = LivingSpace(room_name)

                else:
                    raise Exception("Invalid Room Type.\
                                    Must be office or living")

                Prefix = ("A" if room_type.upper() == "LIVINGSPACE" else "An")
                print("{} {} called {} has been successfully created".format(
                    Prefix, room_type, room_name))

    def add_person(self, arg):
        """The function adds a person to a room randomly."""
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        rank = (arg["<FELLOW/STAFF>"])
        wants_accomodation = (arg["<wants_accomodation>"] or "N")

        if rank.upper() == "STAFF":
            new_user = Staff(first_name, last_name)
            staff_id = "S" + str(new_user.id)
            self.persons[staff_id] = new_user

            print("{0} {1} has been successfully added".format(self.persons[
                staff_id].rank, self.persons[staff_id]))

        elif rank.upper() == "FELLOW":
            new_user = Fellow(first_name, last_name,
                              wants_accomodation.upper())
            fellow_id = "F" + str(new_user.id)
            self.persons[fellow_id] = new_user

            print("{0} {1} has been successfully added".format(self.persons[
                fellow_id].rank, self.persons[fellow_id]))

        else:
            raise Exception('Person can only be a fellow or staff')

        self.assign_person(new_user)

    @staticmethod
    def get_available_room_spaces(room_spaces):
        available_room_spaces = []
        for room, room_info in room_spaces.items():
            if (len(room_info.occupants) < room_info.max_occupants):
                available_room_spaces.append(room_info)
        return available_room_spaces

    def assign_person(self, person):
        """The function randomly assigns a person to a room."""
        available_office_spaces = self.get_available_room_spaces(
            self.office_rooms)
        if available_office_spaces == []:
            print("There is currently no office space")
        else:
            assigned_office_space = random.choice(available_office_spaces)
            assigned_office_space.occupants.append(person)
            person.office_space_allocated = assigned_office_space.room_name
            print("{0} has been allocated the office {1}".format(
                person.first_name, assigned_office_space.room_name))

        if person.wants_accomodation.upper() == "Y":
            available_living_spaces = self.get_available_room_spaces(
                self.living_rooms)
            if available_living_spaces == []:
                print("There is currently no living space")
            else:
                assigned_living_space = random.choice(available_living_spaces)
                assigned_living_space.occupants.append(person)
                person.living_space_allocated = assigned_living_space.room_name
                print("{0} has been allocated the livingspace {1}".format(
                    person.first_name, assigned_living_space.room_name))

    def print_room(self, arg):
        """The function prints the names of\
           all people in the stated room name."""
        room_name = arg["<room_name>"]
        if room_name in self.office_rooms:
            office_room_info = self.office_rooms[room_name]
            print(office_room_info.occupants)

        elif room_name in self.living_rooms:
            living_room_info = self.living_rooms[room_name]
            print(living_room_info.occupants)

        else:
            print("Room does not exist")

    def print_allocations(self, arg):
        """The function prints a list of all\
         allocated rooms with their members."""
        # pdb.set_trace()
        allocation_file = arg["--o"]

        for office_name, office_info in self.office_rooms.items():
            if len(office_info.occupants) != 0:
                if allocation_file is None:

                    print(
                        office_info.room_name + self.divider
                        + str(office_info.occupants) + "\n")
                else:
                    result = open(allocation_file + ".txt", "a")
                    result.write(
                        office_info.room_name + self.divider
                        + str(office_info.occupants) + "\n")
                    result.close()

        for living_name, living_info in self.living_rooms.items():
            if len(living_info.occupants) != 0:
                if allocation_file is None:
                    print(
                        living_info.room_name + self.divider
                        + str(living_info.occupants) + "\n")
                else:
                    result = open(allocation_file + ".txt", "a")
                    result.write(
                        living_info.room_name + self.divider
                        + str(living_info.occupants) + "\n")
                    result.close()

    def print_unallocated(self, arg):
        """ This function prints a list of unallocated\
        persons to either the screen or text file."""

        unallocated_file = arg["--o"]

        for person_name, person_info in self.persons.items():

            if (person_info.wants_accomodation == "N"
                    and person_info.office_space_allocated == ""):
                if unallocated_file is None:
                    print(person_info)
                else:
                    result = open(unallocated_file + ".txt", "a")
                    result.write("\n"(str(person_info)))
                    result.close()

            elif (person_info.wants_accomodation == "Y"
                    and person_info.living_space_allocated == ""):
                if unallocated_file is None:
                    print(person_info)
                else:
                    result = open(unallocated_file + ".txt", "a")
                    result.write("\n"(str(person_info)))
                    result.close()
            else:
                print("Everyone has been allocated")
