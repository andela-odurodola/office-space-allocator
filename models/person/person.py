class Person(object):

    def __init__(self, first_name, last_name, wants_accomodation):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.full_name = first_name + " " + last_name
        self.wants_accomodation = wants_accomodation or "N"
        self.office_space = ""
