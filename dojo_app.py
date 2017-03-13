#!/usr/local/bin/python3
"""
This Application automatically allocated spaces to people at random
Usage:
    dojo_app.py create_room <room_type> <room_name>...
    dojo_app.py add_person <first_name> <last_name> <FELLOW/STAFF> [<wants_accomodation>]
    dojo_app.py print_room <room_name>
    dojo_app.py print_allocations [--o=filename]
    dojo_app.py print_unallocated [--o=filename]
    dojo_app.py reallocate_person <person_identifier> <new_room_name>​
    dojo_app.py load_people <text_file>
    dojo_app.py save_state [--db=sqlite_database]
    dojo_app.py load_state <sqlite_database>
    dojo_app.py -h | --help
    dojo_app.py -V | --version
    dojo_app.py -i | --interactive

Options:
    -o                      Outputs the result into a text file.
    -h, --help              Show message and exit.
    -V, --version           Show the version.
    -i, --interactive       interactive.


"""
import cmd
import sys

from docopt import docopt, DocoptExit
from models.dojo import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoRoom(cmd.Cmd):
    """Welcome to the Dojo Room App!"""
    prompt = '(Dojo) '
    dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type>  <room_name>..."""
        self.dojo.create_room(arg)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <FELLOW/STAFF> [<wants_accomodation>]"""
        self.dojo.add_person(arg)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        self.dojo.print_room(arg)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=filename]"""
        self.dojo.print_allocations(arg)
        # print(arg)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=filename]"""
        self.dojo.print_unallocated(arg)
        # print(arg)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        self.dojo.reallocate_person(arg)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <text_file>"""
        self.dojo.load_people(arg)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=sqlite_database]"""
        self.dojo.save_state(arg)

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""
        self.dojo.load_state(arg)

    def do_q(self, arg):
        """Quits out of Interactive Mode."""
        exit()


opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
    DojoRoom().cmdloop()

# print(opt)
