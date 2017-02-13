class Dojo(object):

    def create_room(self, arg):
        self.room_name = arg["<room_name>"]
        for name in self.room_name:
            print("An " + arg["<room_type>"] + " called " +
                  name + " has been successfully created!")

    def add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <fellow/staff> [<wants_accomodation>]"""
        self.first_name = arg["first_name>"]
        self.last_name = arg["last_name>"]
        self.first_name = arg["first_name>"]
        self.first_name = arg["first_name>"]

        print("Staff Neil Armstrong has been successfully added")
