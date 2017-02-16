import person

class Fellow(Person):
    def __init__(self,arg,office_name,living_name):
        Person.__init__(self,arg)
        self.office_name = office_name
        self.living_name = living_name
        