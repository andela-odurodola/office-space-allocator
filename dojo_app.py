"""
This Application automatically allocated spaces to people at random
Usage:
    dojo_app.py create_room <room_type> <room_name>...
    dojo_app.py add_person <first_name> <last_name> (fellow|staff) [<wants_accomodation>]
    dojo_app.py -h | --help
    dojo_app.py -V | --version
    dojo_app.py -i | --interactive   

Options:
    -h, --help              Show message and exit.
    -V, --version           Show the version.
    -i, --interactive       interactive.
    --wants_accomodation    [default: N].

"""
import sys
import cmd
from docopt import docopt, DocoptExit
from models.dojo import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            result = docopt(fn.__doc__, arg)

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

        return func(self, result)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoRoom(cmd.Cmd):
    """Welcome to the Dojo Room App!"""
    prompt = '(Dojo) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type>  <room_name>..."""
        # Dojo().create_room(arg)

    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> (fellow|staff) [<wants_accomodation>]"""
        

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        exit()


if __name__ == '__main__':
    result = docopt(__doc__, sys.argv[1:], version=1.0)

    if result['--interactive']:
        DojoRoom().cmdloop()

    print(result)
