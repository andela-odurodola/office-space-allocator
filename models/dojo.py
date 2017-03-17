#!/usr/local/bin/python3
import os
import random
import sys

from os import path


sys.path.append(os.path.join(path.dirname(path.abspath(__file__))))

from database_model.database_states import DatabaseManager, OfficeRooms,\
                                            LivingRooms, Persons
from person.person import Fellow, Person, Staff
from room.room import LivingSpace, Office, Room



class Dojo(object):

    office_rooms = []
    living_rooms = []
    persons = []
    divider = ("\n{}\n".format("-" * 30))
    unallocated_officelist = []
    unallocated_livinglist = []

    def create_room(self, room_type, room_names):
        # The function creates a new room.

        if not (room_type.upper() in ["OFFICE", "LIVINGSPACE"]):
            raise ValueError("Invalid Room Type.Must be office or living")

        for room_name in room_names:
            if room_name in self.get_all_room_names():
                print("The room {} exists. Try again".format(room_name))
            else:
                if room_type.upper() == "OFFICE":
                    self.office_rooms.append(Office(room_name))
                elif room_type.upper() == "LIVINGSPACE":
                    self.living_rooms.append(LivingSpace(room_name))
                prefix = "A" if room_type.upper() == "LIVINGSPACE" else "An"
                print("{} {} called {} has been successfully created".format(
                    prefix, room_type, room_name))

    def get_all_room_names(self):
        return [room.room_name for room in self.living_rooms + self.office_rooms]

    def add_person(self, first_name, last_name, rank, wants_accomodation):
        # The function adds a person to a room randomly
        if rank.upper() == "STAFF":
            new_user = Staff(first_name, last_name)

        elif rank.upper() == "FELLOW":
            new_user = Fellow(first_name, last_name,
                              wants_accomodation)
        else:
            raise Exception('Person can only be a fellow or staff')

        self.persons.append(new_user)
        print("{0} {1} has been successfully added with id {2}".format(new_user.rank, new_user, new_user.identifier))
        self.assign_person(new_user)

    @staticmethod
    def get_available_room_spaces(room_spaces):
        # It gets a list of available rooms for allocation
        available_room_spaces = [room for room in room_spaces if (len(room.occupants) <
                                 room.max_occupants)]
        return available_room_spaces

    @staticmethod
    def assign_space_to_person(room_spaces, person, flag=None):
        # It randomly choose an available room
        available_space = random.choice(room_spaces)
        available_space.occupants.append(person)
        if available_space.room_type == "OFFICE":
            person.office_space_allocated = available_space
        else:
            person.living_space_allocated = available_space

        print("{0} has been allocated the {1} {2}".format(
            person.first_name, available_space.room_type.lower(), available_space.room_name))

    def assign_person(self, person):
        # The function randomly assigns a person to a room.
        available_office_spaces = self.get_available_room_spaces(
            self.office_rooms)
        if available_office_spaces:
            self.assign_space_to_person(available_office_spaces, person)
        else:
            self.unallocated_officelist.append(person)
            print("There is currently no office space")

        flag = person.wants_accomodation
        if flag == 'y':
            available_living_spaces = self.get_available_room_spaces(
                self.living_rooms)
            if available_living_spaces:
                self.assign_space_to_person(available_living_spaces, person, flag='y')
            else:
                self.unallocated_livinglist.append(person)
                print("There is currently no living space")

    def get_room_occupants(self, room_name):
        # It returns a list of both room occupants
        room_occupants, = [room.occupants for room in self.office_rooms +
                           self.living_rooms if room.room_name.lower() == room_name.lower()]
        return room_occupants

    def print_room(self, room_name):
        # It prints a list of room members.
        if not(room_name in self.get_all_room_names()):
            raise ValueError("The room {} has not been created".format(room_name))
        room_occupants = self.get_room_occupants(room_name)
        if room_occupants:
            print('Room occupants --- {}'.format(room_occupants))
        else:
            print("The room {} is empty".format(room_name))

    def print_allocations(self, allocation_file=None):
        # It prints a list of all allocated rooms with their members
        for room in self.office_rooms + self.living_rooms:
            if room.occupants:
                output = (room.room_name + self.divider + str(room.occupants) + '\n')
                if allocation_file is None:
                    print(output)
                else:
                    with open(allocation_file + '.txt', 'w') as allocated:
                        allocated.write(output)

    def print_unallocated(self, unallocated_file=None):
        # It prints a list of unallocated persons to either the screen or text file
        if self.unallocated_officelist or self.unallocated_livinglist:
            unallocated_office = ("Unallocated persons for office rooms----{}".format(self.unallocated_officelist))
            unallocated_living = ("Unallocated persons for living rooms----{}".format(self.unallocated_livinglist))
            if unallocated_file is None:
                print(unallocated_office)
                print(unallocated_living)
            else:
                with open(unallocated_file + '.txt', 'w') as unallocated:
                    unallocated.write(unallocated_office + '\n' + unallocated_living)
        else:
            print("Everyone has been allocated")

    def get_person(self, person_id):
        person_list = [person for person in self.persons if person.identifier == person_id]
        if person_list:
            return person_list[0]


    def get_room(self, room_name):
        room_list = [room for room in self.living_rooms + self.office_rooms if room_name.lower() == room.room_name.lower()]
        if room_list:
            return room_list[0]


    def get_members_of_a_room(person, room_name):
        if person in self.get_room_occupants:
            return True

    def reallocate_person(self, person_id, new_room_name):
        # The function reallocates a person with id to a new room
        person = self.get_person(person_id)
        room = self.get_room(new_room_name)
        reallocate_map = {"OFFICE": Office, "LIVINGSPACE": LivingSpace}
        unallocated_list_map = {"OFFICE": Dojo.unallocated_officelist, "LIVINGSPACE": Dojo.unallocated_livinglist}

        if person and room:
            try:
                room.check_availability()
                room.is_member(person)
                reallocate_map[room.room_type].reallocate_person(person, room, unallocated_list_map[room.room_type])
            except ValueError as e:
                print(e)
        else:
            print ("Person with the id {} or room {} does not exist".format(person_id, new_room_name))

    def load_people(self, filename):
        # The function adds people to a room from a text file
        # checks if the file exist
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                people_info = f.readlines()

            for line in people_info:
                person_info = line.split()

                if len(person_info) == 3:
                    self.add_person(person_info[0], person_info[1], person_info[2], '')

                elif len(person_info) == 4:
                    self.add_person(person_info[0], person_info[1], person_info[2], person_info[3])
        else:
            print("The filename {} does not exist".format(filename))

    def save_state(self, database_name):
        # It saves all data into an sqlite database
        if database_name is None:
            database_name = 'database_model/dojo.db'
        else:
            database_name = 'database_model/' + database_name + '.db'

        database = DatabaseManager(database_name)
        database_session = database.session()

        officespace_details = OfficeRooms(room_info=self.office_rooms)
        database_session.add(officespace_details)
        database_session.commit()

        livingspace_details = LivingRooms(livingspace_info=self.living_rooms)
        database_session.add(livingspace_details)
        database_session.commit()

        persons_details = Persons(person_info=self.persons)
        database_session.add(persons_details)
        database_session.commit()

    def load_state(self, database_file):
        # It loads saved data from the database specified
        path = 'database_model/' + database_file
        if os.path.exists(path):

            database = DatabaseManager(path)
            database_session = database.session()

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
