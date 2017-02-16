class Person(object):
    
    def __init__(self, arg):
        self.first_name = arg["<first_name>"]
        self.last_name = arg["<last_name>"]
        self.rank = arg["<FELLOW/STAFF>"]
        self.wants_accomodation = arg["<wants_accomodation>"]
