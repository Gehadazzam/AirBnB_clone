#!/usr/bin/python3
"""make a command interpreter using cmd module"""


import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    """class to handle the program"""

    prompt = "(hbnb) "

    def default(self, line):
        """default action when there is no matching command"""
        console_default = {
            "create": self.do_create,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "quit": self.do_quit,
            "count": self.do_count,
            "EOF": self.do_EOF,
            "emptyline": self.emptyline,
        }
        self.check_command(line, console_default)

    def check_command(self, line_command, console_default):
        """checks for valid command and prints help if needed"""
        period = re.match(r"(\w+)\.(\w+)(?:\((.*?)\))?(?:\.(.*?))?(?:\.(.*?))?", line_command)
        if period:
            class_name = period.group(1)
            method = period.group(2)
            id_arg = period.group(3)
            attribute1 = period.group(4)
            attribute2 = period.group(5)
            if method and class_name:
                if attribute1 and attribute2 and id_arg:
                    if '"' in id_arg and '"' in attribute1 and '"' in attribute2:
                        hack = (("{} {} {} {} {}").format(method, class_name, id_arg[1:-1], attribute1[1:-1], attribute2[1:-1]))
                    else:
                        hack = (("{} {} {} {} {}").format(method, class_name, id_arg, attribute1, attribute2))
                elif id_arg:
                    if '"' in id_arg:
                        hack = (("{} {} {}").format(method, class_name, id_arg[1:-1]))
                    else:
                        hack = (("{} {} {}").format(method, class_name, id_arg))
                else:
                    hack = (("{} {}").format(method, class_name))
                self.onecmd(hack)
                return hack
            else:
                print("*** Unknown syntax: {}".format(line_command))

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

    def do_count(self, ar):
        """retrive the number of instances of a class"""
        par = ar.split()
        if not par:
            print("** class name missing **")
        elif not par[0] in storage.class_dict():
             print("** class doesn't exist **")
        else:
            count = [item for item in storage.all() if item.startswith(par[0] + '.')]
            print(len(count))

if __name__ == "__main__":
    HBNBCommand().cmdloop()