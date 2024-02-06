#!/usr/bin/python3
"""make a command interpreter using cmd module"""


import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.class_dict():
            print ("** class doesn't exist **")
        else:
            l = storage.class_dict()[arg]()
            l.save()
            print(l.id)

    def do_show(self, arg):
        """Prints the string representation the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            w = arg.split()
            if w[0] not in storage.class_dict():
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
            if w[0] not in storage.class_dict():
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

    def do_destroy(self, arg):
        """if the class exist destroy it"""
        if not arg:
            print("** class name missing **")
        else:
            w = arg.split()
            if w[0] not in storage.class_dict():
                print("** class doesn't exist **")
            elif len(w) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(w[0], w[1])
                if k in storage.all():
                    del storage.all()[k]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg:
            w = arg.split()
            if w[0] not in storage.class_dict():
                print("** class doesn't exist **")
            else:
                print([str(v) for k, v in storage.all().items()
                      if type(v).__name__ == w[0]])
        else:
            print([str(v) for k, v in storage.all().items()])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
