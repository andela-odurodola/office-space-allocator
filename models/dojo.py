#!/usr/bin/python3
class Dojo(object):
    
    # wriite  a constructor 

    def create_room(self, arg):
        self.room_type = arg["<room_type>"]
        self.room_name = arg["<room_name>"]
        for name in self.room_name:
            # print("An " + arg["<room_type>"] + " called " +
            #       name + " has been successfully created!")
            print("A %s called %s has been successfully created" % (self.room_type, name))

    def add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <fellow/staff> [<wants_accomodation>]"""
        self.first_name = arg["<first_name>"]
        self.last_name = arg["<last_name>"]
        self.rank = (arg["<fellow/staff>"])
        self.wants_accomodation = arg["<wants_accomodation>"]

        if self.rank == 'fellow':
            print("fellow is added")
            print("%s %s %s has been successfully added" % (self.rank, self.first_name, self.last_name))
        elif self.rank == "staff":
            # print(self.rank, "Staff is Added")
            print("%s %s %s has been successfully added" % (self.rank, self.first_name, self.last_name))
        else:
            print("Invalid Person")
        # print(type(self.rank))

        # print("Staff Neil Armstrong has been successfully added")
        # Neil has been allocated the office Blue
