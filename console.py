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
        self.check_command(line)

    def check_command(self, line_command):
        """checks for valid command and prints help if needed"""
        period = re.match(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line_command)
        if period:
            class_name = period.group(1)
            method = period.group(2)
            id_arg = period.group(3)
            if method == "update":
                if '{' in id_arg and '}' in id_arg:
                    id_arg = id_arg.replace("'", '"')
                    id_arg = id_arg.replace(": ", ', ')
                    id_attribute, id_arg = id_arg.split(sep=", {")
                    id_arg = id_arg[:-1]
                    if '"' in id_attribute:
                        id_attribute = id_attribute[1:-1]
                    id_arg = id_arg.split(sep=", ")
                    for i in range(0, len(id_arg), 2):
                        key = id_arg[i]
                        value = id_arg[i+1]
                        if '"' in key:
                            key = key[1:-1]
                        hack = (("{} {} {} {} {}".format(
                            method, class_name, id_attribute, key, value
                        )))
                        self.onecmd(hack)
                    return hack
                if ', ' in id_arg:
                    id_attribute, key_attr, value_attr = id_arg.split(sep=", ")
                if '"' in id_attribute:
                    id_attribute = id_attribute[1:-1]
                if '"' in key_attr:
                    key_attr = key_attr[1:-1]
                all = (("{} {} {} {} {}".format(
                    method, class_name, id_attribute,
                    key_attr, value_attr
                    )))
                self.onecmd(all)
                return all
            elif method != "update":
                if id_arg and class_name:
                    if '"' in id_arg:
                        all = (("{} {} {}").format(
                          method, class_name, id_arg[1:-1]
                        ))
                    else:
                        all = (("{} {} {}").format(method, class_name, id_arg))
                else:
                    all = (("{} {}").format(method, class_name))
                self.onecmd(all)
                return all
            else:
                print("*** Unknown syntax: {}".format(line_command))
        else:
            return line_command

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
            print("** class doesn't exist **")
        else:
            line = storage.class_dict()[arg]()
            line.save()
            print(line.id)

    def do_show(self, arg):
        """Prints the string representation the class name and id"""
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
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_update(self, arg):
        """Updates an instance adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            pattern =\
              r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
            match = re.search(pattern, arg)
            classname_attribute = match.group(1)
            uid_attribute = match.group(2)
            key_attr = match.group(3)
            value_attr = match.group(4)
            if not match:
                print("** class name missing **")
            if classname_attribute not in storage.class_dict():
                print("** class doesn't exist **")
            elif not uid_attribute:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(classname_attribute, uid_attribute)
                if k not in storage.all():
                    print("** no instance found **")
                elif not key_attr:
                    print("** attribute name missing **")
                elif not value_attr:
                    print("** value missing **")
                else:
                    attributes = storage.attribe()[classname_attribute]
                    if key_attr in attributes:
                        value_attr =\
                          attributes[key_attr](value_attr)
                    if '"' in value_attr:
                        value_attr = value_attr[1:-1]
                    else:
                        if '.' in value_attr:
                            value_attr = float(value_attr)
                        else:
                            value_attr = int(value_attr)
                    setattr(storage.all()[k], key_attr, value_attr)
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
            count = [
              item for item in storage.all() if item.startswith(par[0] + '.')
            ]
            print(len(count))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
