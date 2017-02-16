import person

class Staff(Person):
    def __init__(self, arg, office_name):
        Person.__init__(self, arg)
        self.office_name = office_name
        