from models.person.person import Person


class Staff(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, "N")
        self.rank = "STAFF"
