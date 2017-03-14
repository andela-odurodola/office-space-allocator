#!/usr/local/bin/python3
import os
import random


from database_model.database_states import DatabaseManager, OfficeRooms,\
                                            LivingRooms, Persons
from models.room.living_space import LivingSpace
from models.room.office_space import Office
from models.person.fellow import Fellow
from models.person.staff import Staff


class Dojo(object):
    """The Dojo class."""

    office_rooms = {}
    living_rooms = {}
    persons = {}
    divider = ("\n{}\n".format("-" * 30))

    def create_room(self, arg):
        """The function creates a new room."""
        room_type = arg["<room_type>"]
        room_names = arg["<room_name>"]

        for room_name in room_names:
            if room_name in ['office', 'livingspace']:
                raise ValueError("This is not a valid room name")
            else:
                if room_type.upper() == "OFFICE":
                    self.office_rooms[room_name] = Office(room_name)
                elif room_type.upper() == "LIVINGSPACE":
                    self.living_rooms[room_name] = LivingSpace(room_name)
                else:
                    raise ValueError("Invalid Room Type.Must be office or living")
                prefix = "A" if room_type.upper() == "LIVINGSPACE" else "An"
                print("{} {} called {} has been successfully created".format(
                    prefix, room_type, room_name))

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
        """It gets a list of available rooms for allocation."""
        available_room_spaces = [room_info for room_info in room_spaces.
                                 values() if (len(room_info.occupants) <
                                              room_info.max_occupants)]
        return available_room_spaces

    def assign_person(self, person):
        """The function randomly assigns a person to a room."""
        available_office_spaces = self.get_available_room_spaces(
            self.office_rooms)
        if available_office_spaces:
            assigned_office_space = random.choice(available_office_spaces)
            assigned_office_space.occupants.append(person)
            person.office_space_allocated = assigned_office_space.room_name
            print("{0} has been allocated the office {1}".format(
                person.first_name, assigned_office_space.room_name))
        else:
            print("There is currently no office space")
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
        """It prints the names of occupantsstated room name."""
        room_name = arg["<room_name>"]
        if room_name in self.office_rooms:
            office_room_info = self.office_rooms[room_name]
            if office_room_info.occupants == []:
                raise Exception("Office room is empty")
            else:
                print('Office room occupants --- {}'.format(office_room_info.occupants))
        elif room_name in self.living_rooms:
            living_room_info = self.living_rooms[room_name]
            if living_room_info.occupants == []:
                raise Exception("Living room is empty")
            else:
                print('Living room occupants --- {}'.format(living_room_info.occupants))
        else:
            raise Exception("The room has not been created")

    def print_allocations(self, arg):
        """The function prints a list of all
         allocated rooms with their members."""
        allocation_file = arg["--o"]

        for office_name, office_info in self.office_rooms.items():
            if office_info.occupants:
                if allocation_file is None:
                    print(
                        office_info.room_name + self.divider
                        + str(office_info.occupants) + "\n")
                else:
                    with open(allocation_file + ".txt", "w") as result:
                        result.write(office_info.room_name + self.divider
                                     + str(office_info.occupants))

        for living_name, living_info in self.living_rooms.items():
            if len(living_info.occupants) != 0:
                if allocation_file is None:
                    print(living_info.room_name + self.divider
                          + str(living_info.occupants) + "\n")
                else:
                    with open(allocation_file + ".txt", "w") as result:
                        result.write(living_info.room_name + self.divider
                                     + str(living_info.occupants))

    def print_unallocated(self, arg):
        """
        The function prints a list of unallocated
        persons to either the screen or text file.
        """
        unallocated_file = arg["--o"]
        for person_name, person_info in self.persons.items():

            if (person_info.wants_accomodation == "N"
                    and person_info.office_space_allocated == ""):
                if unallocated_file is None:
                    print("Unallocated persons ----{}".format(person_info))
                else:
                    with open(unallocated_file + ".txt", "w") as result:
                        result.write("Unallocated persons ----{}".format(person_info))
            elif (person_info.wants_accomodation == "Y"
                    and person_info.living_space_allocated == ""):
                if unallocated_file is None:
                    print("Unallocated persons ----{}".format(person_info))
                else:
                    with open(unallocated_file + ".txt", "w") as result:
                        result.write("Unallocated persons ----{}".format(person_info))
            else:
                print ("Everyone has been allocated")

    def reallocate_person(self, arg):
        """The function reallocates a person with id to a new room."""
        person_id = arg["<person_identifier>"]
        new_room_name = arg["<new_room_name>"]

        if (person_id in self.persons.keys()) and (new_room_name in
                                                   (self.office_rooms.keys() or self.living_rooms.keys())):

            if ((new_room_name == self.persons[person_id].office_space_allocated)\
                or (new_room_name == self.persons[person_id].\
                    living_space_allocated)):
                print ("Person {} is already a member of room {}".format(
                    person_id, new_room_name))
            else:
                if new_room_name in self.office_rooms.keys():
                    if (len(self.office_rooms[new_room_name].occupants) < self.
                            office_rooms[new_room_name].max_occupants):
                        if self.persons[person_id].office_space_allocated:
                            old_room_name = self.office_rooms[
                                self.persons[person_id].office_space_allocated]
                            old_room_name.occupants.remove(
                                self.persons[person_id])

                            self.persons[
                                person_id].office_space_allocated = self.\
                                office_rooms[new_room_name].room_name
                            self.office_rooms[new_room_name].occupants.\
                                append(self.persons[person_id])
                        else:
                            self.persons[person_id].office_space_allocated =\
                                self.office_rooms[new_room_name].room_name
                            self.office_rooms[new_room_name].occupants.\
                                append(self.persons[person_id])

                        print("identifier {0} has been reallocated to the office {1}"
                              .format(person_id, self.persons[person_id].
                                      office_space_allocated))
                    else:
                        print("{} is full".format(new_room_name))
                else:
                    if (len(self.living_rooms[new_room_name].occupants) < self.
                            living_rooms[new_room_name].max_occupants):
                        if self.persons[person_id].living_space_allocated:
                            old_room_name = self.living_rooms[
                                self.persons[person_id].living_space_allocated]
                            old_room_name.occupants.remove(
                                self.persons[person_id])

                            self.persons[person_id].living_space_allocated =\
                                self.living_rooms[new_room_name].room_name
                            self.living_rooms[new_room_name].occupants.\
                                append(self.persons[person_id])
                        else:
                            self.persons[person_id].living_space_allocated =\
                             self.living_rooms[new_room_name].room_name
                            self.living_rooms[new_room_name].occupants.\
                                append(self.persons[person_id])
                        print("identifier {0} has been reallocated to the livingroom {1}"
                              .format(person_id, self.persons[person_id].
                                      living_space_allocated))
                    else:
                        print("{} is full".format(new_room_name))

        else:
            print ("Person {} does not exist or room name is invalid".format(person_id))

    def load_people(self, arg):
        """The function adds people to a room from a text file."""
        name_of_file = arg["<text_file>"]

        with open(name_of_file, "r") as f:
            people_info = f.readlines()

        for line in people_info:
            person_info = line.split()
            # import pdb; pdb.set_trace()
            if len(person_info) == 4:
                first_name, last_name, rank, wants_accomodation = person_info[
                    :4]
                person = {
                    "<first_name>": first_name,
                    "<last_name>": last_name,
                    "<FELLOW/STAFF>": rank,
                    "<wants_accomodation>": wants_accomodation
                }
            elif len(person_info) == 3:
                first_name, last_name, rank = person_info[
                    :3]
                person = {
                    "<first_name>": first_name,
                    "<last_name>": last_name,
                    "<FELLOW/STAFF>": rank,
                    "<wants_accomodation>": ''
                }

            self.add_person(person)

    def save_state(self, arg):
        """It saves all data into an sqlite database."""
        database_name = arg["--db"]

        if database_name is None:
            database_name = 'database_model/dojo.db'
        else:
            database_name = 'database_model/' + database_name + '.db'

        database = DatabaseManager(database_name)
        database_session = database.Session()

        officespace_details = OfficeRooms(room_info=self.office_rooms)
        database_session.add(officespace_details)
        database_session.commit()

        livingspace_details = LivingRooms(livingspace_info=self.living_rooms)
        database_session.add(livingspace_details)
        database_session.commit()

        persons_details = Persons(person_info=self.persons)
        database_session.add(persons_details)
        database_session.commit()

    def load_state(self, arg):
        """It loads saved data from the database specified."""
        database_file = arg["<sqlite_database>"]
        path = 'database_model/' + database_file
        if os.path.exists(path):

            database = DatabaseManager(path)
            database_session = database.Session()

            for row in database_session.query(OfficeRooms):
                self.office_rooms = row.room_info
                print(self.office_rooms)

            for row in database_session.query(LivingRooms):
                self.living_rooms = row.livingspace_info
                print(self.living_rooms)

            for row in database_session.query(Persons):
                self.persons = row.person_info
                print(self.persons)
        else:
            raise Exception("File does not exist.")
