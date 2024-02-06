#!/usr/bin/python3
"""make a command interpreter using cmd module"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class to handle the program"""

    prompt = "(hbnb) "

    def do_quit(self, ar):
        """quit the command interpreter"""

        return True

    def do_EOF(self, ar):
        """print new line and exit"""

        print()
        return True

    def emptyline(self):
        """nothing just pass"""

        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
