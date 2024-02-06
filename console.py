#!/usr/bin/python3
"""make a command interpreter using cmd module"""


import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """class to handle the program"""

    prompt = "(hbnb) "
    # List of classes
    cls = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in {'BaseModel'}:
            print ("** class doesn't exist **")
        else:
            i = BaseModel()
            i.save()
            print(i.id)

    def do_show(self, arg):
        """Prints the string representation the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            w = arg.split()
            if w[0] not in {'BaseModel'}:
                print ("** class doesn't exist **")
            elif len(w) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(w[0], w[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_update(self, arg):
        """Updates an instance adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            w = arg.split()
            if w[0] not in {'BaseModel'}:
                print ("** class doesn't exist **")
            elif len(w) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(w[0], w[1])
                if k not in storage.all():
                    print("** no instance found **")
                elif len(w) < 3:
                    print("** attribute name missing **")
                elif len(w) < 4:
                    print("** value missing **")
                else:
                    setattr(storage.all()[k], w[2], w[3])
                    storage.all()[k].save()
    def do_destroy(self, ar):
        """if the class exist destroy it"""

        par = ar.split()
        if not ar:
            """just print a massage and return"""

            print("** class name missing **")
            return
        elif not par[0] in HBNBCommand.cls:
            """check if the argument one of our cls"""

            print("** class doesn't exist **")
        elif not par[1]:
            """check if the id is written"""

            print("** instance id missing **")

        else:
            k = par[0] + "." + par[1]
            if k in storage.all():
                """if it existes in the storage"""
                storage.all().pop(k)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, ar):
        """Prints all string representation of all instances"""

        par = ar.split()
        if len(par) < 1:
            """if it is just add print everything"""
            print([str(key) for key in storage.all().items()])

        else:
            if not par[0] in HBNBCommand.cls:
                """if the word after all not a class name"""
                print("** class doesn't exist **")
                return
            else:
                print([str(key) for key in storage.all().items()])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
