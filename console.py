#!/usr/bin/python3

import cmd
import models
from models import storage
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter"""
    prompt = "(hbnb)"

    def empty_line(self):
        """
        Do nothing when empty line is entered
        """
        pass

    def do_quit(self, arg):

        return True

    def help_quit(self, arg):
        print("Quit command to exit the program")
    def do_create(self, arg):
        """
        create a new Basemodel and save it to JSON file
        Usage: create <class_name>
        """
        pass

    def do_show(self, arg):
            """
            Show the string representation of an instance
            Usage: show <class_name> <id>
            """
            pass

    def do_destroy(self, arg):
            """
            Delete an instance based on the class name and id
            Usage: destroy <class_name> <id>
            """
            pass

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class
        Usage: all[class_name]
        """
        pass

    def do_update(seld, arg):
        """
        Update an instance by adding or updating an attribute
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        pass

    def do_EOF(self, arg):
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
