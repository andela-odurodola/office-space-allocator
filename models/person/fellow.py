from models.person.person import Person


class Fellow(Person):

    def __init__(self, first_name, last_name, wants_accomodation):
        super().__init__(first_name, last_name, wants_accomodation)
        self.rank = "FELLOW"
        self.living_space_allocated = ""
