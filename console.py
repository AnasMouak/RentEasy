#!./venv/bin/python
"""
This script defines a HBNBCommand class .
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.car_maker import CarMaker
from models.car_model import CarModel
from models.booking import Booking
from models.contact import Contact
from models.review import Review
from models import storage
import re


class RENTEASYCommand(cmd.Cmd):
    """
    Command line interpreter for RentEasy project.
    """
    
    prompt = '(RentEasy) '
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True
    
    def emptyline(self):
        """Does nothing on empty input."""
        pass

    def precmd(self, line):
        """
        Preprocesses command before executing.

        Args:
            line (str): The command entered by the user.

        Returns:
            str: The processed command.
        """
        match_all = re.match(r'^([A-Za-z]+)\.all\(\)$', line)
        match_count = re.match(r'^([A-Za-z]+)\.count\(\)$', line)
        class_list = ["BaseModel", "User", "CarMaker", "CarModel", 
                      "Booking", "Review"]
    
        if match_all:
            classname = match_all.group(1)
            if classname in class_list:
                instances = storage.all()
                filtered_instances = [str(instance) for key, instance in 
                                      instances.items() if
                                      key.startswith(classname + ".")]

                print(filtered_instances)
                return ''  
            else:
                return ''  
        elif match_count:
            classname = match_count.group(1)
            if classname in class_list:
                count = sum(1 for key in 
                            storage.all().keys() if
                            key.startswith(classname + "."))
                
                print(count)
                return ''  
            else:
                return ''  

        return line
    
    def do_create(self, command):
        """
        Creates a new instance of the specified class with given parameters.

        Args:
            command (str): The full command containing the class name and parameters.

        Returns:
            None
        """
        parts = command.split(" ")
        classname = parts[0]
        params = parts[1:]

        if not classname:
            print("** class name missing **")
            return

        classes = {"BaseModel": BaseModel, "User": User, "CarMaker": CarMaker,
                   "CarModel": CarModel, "Booking": Booking, "Contact": Contact}

        if classname not in classes:
            print("** class doesn't exist **")
            return

        instance = classes[classname]()

        for param in params:
            key, _, value = param.partition('=')
            if not key or not value:
                continue

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue

            setattr(instance, key, value)

        storage.new(instance)
        instance.save()
        print(instance.id)

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and ID.

        Args:
            args (str): The command arguments.

        Returns:
            None
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        else:
            if (args[0] != "BaseModel" and args[0] != "User" and 
                args[0] != "CarMaker" and args[0] != "CarModel" and 
                args[0] != "Booking" and args[0] != "Contact"):

                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                    if (not re.match(r, str(args[1])) or
                        args[0] + "." + args[1] not in 
                            storage.all()):
                        
                        print("** no instance found **")
                    else:
                        key = args[0] + "." + args[1]
                        storage.delete(storage.all()[key])
                        storage.save()
    
    def do_show(self, args):
        """
        Displays the string representation of an instance.

        Args:
            args (str): The command arguments.

        Returns:
            None
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        else:
            if (args[0] != "BaseModel" and args[0] != "User" and 
                args[0] != "CarMaker" and args[0] != "CarModel" and 
                args[0] != "Booking" and args[0] != "Contact"):
                
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                    if (not re.match(r, str(args[1])) or 
                        args[0] + "." + args[1] not in 
                            storage.all()):
                        
                        print("** no instance found **")
                    else:
                        key = args[0] + "." + args[1]
                        instance = storage.all()[key]
                        print(instance)

    def do_all(self, classname):
        """
        Displays all string representations of instances.

        Args:
            classname (str): The name of the class.

        Returns:
            None
        """
        if not classname:
            instances = storage.all()
            all_instances = [str(instance) for instance in instances.values()]
            print(all_instances)
        elif (classname == "BaseModel" or classname == "User"or
              classname == "CarMaker" or classname == "CarModel" or
              classname == "Booking" or classname == "Contact"):
            
            instances = storage.all()
            filtered_instances = [str(instance) for key, instance in 
                                  instances.items() if 
                                  key.startswith(classname + ".")]
            
            print(filtered_instances)
        else:
            print("** class doesn't exist **")


    def do_update(self, args):        
        """
        Updates an instance attribute value.

        Args:
            args (str): The command arguments.

        Returns:
            None
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        else:
            if (args[0] != "BaseModel" and args[0] != "User" and 
                args[0] != "CarMaker" and args[0] != "CarModel" and 
                args[0] != "Booking" and args[0] != "Contact" ):
                
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    if len(args) < 3:
                        r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                        if (not re.match(r, str(args[1])) or 
                            args[0] + "." + args[1] not in 
                                storage.all()):
                            
                            print("** no instance found **")
                        else:
                            print("** attribute name missing **")
                    else:
                        if len(args) < 4:
                            print("** value missing **")
                        else:
                            r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                            if (not re.match(r, str(args[1])) or 
                                args[0] + "." + args[1] not in 
                                    storage.all()):
                            
                                print("** no instance found **")
                            else:
                                key = args[0] + "." + args[1]
                                instance = storage.all()[key]
                                setattr(instance, args[2], args[3]) 
                                storage.save()

    
    def do_count(self, classname):
        """
        Counts the number of instances of a class.

        Args:
            classname (str): The name of the class.

        Returns:
            None
        """
        if not classname:
            print("** class name missing **")
        else:
            if classname in ["BaseModel", "User", "CarMaker", "CarModel",
                             "Booking", "Contact"]:
                count = 0
                for key in storage.all().keys():
                    if key.startswith(classname + "."):
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    RENTEASYCommand().cmdloop()
