[![Coverage Status](https://coveralls.io/repos/github/andela-odurodola/office-space-allocator/badge.svg?branch=master)](https://coveralls.io/github/andela-odurodola/office-space-allocator?branch=master)

### Dojo-Room-Allocator
A Python Command Line Interface application for allocating rooms to both fellows and staffs of Dojo (Andela Kenya facility). It can be used to allocate fellows and staffs to offices or living spaces. Offices and living spaces can be created and Fellows and Staffs can be added to the rooms. Fellows and Staffs are allocated to offices by default, while fellows can choose whether they want a living space or not. Offices can occupy a maximum of six persons while living spaces can occupy a maximum of four persons.

###Installation
*Clone the repo git clone (https://github.com/andela-odurodola/office-space-allocator.git/) and navigate to the project directory

*Install dependencies pip install -r requirements.txt

*Run the program python dojo_app.py shows a list of available commands
**

###Usage
```
dojo_app.py create_room <room_type> <room_name>...
dojo_app.py add_person <first_name> <last_name> <FELLOW/STAFF> [<wants_accomodation>]
dojo_app.py print_room <room_name>
dojo_app.py print_allocations [--o=filename]
dojo_app.py print_unallocated [--o=filename]
dojo_app.py reallocate_person <person_identifier> <new_room_name>
dojo_app.py load_people <text_file>
dojo_app.py -h | --help
dojo_app.py -V | --version
dojo_app.py -i | --interactive
```

###Running tests
+ Navigate to the project directory

+ Run nosetests testfilename to run test

###References
(https://github.com/docopt/docopt)

(http://docopt.org/)

(https://docs.python.org)

###Author
Damilola Durodola
