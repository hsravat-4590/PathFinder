import os
import json
import sys
import importlib

class Index:
    # Index Class hosting all commands
    Command = 'pathfinder'
    index = 'src/shell/index'

    def __init__(self, command):
        self.Command = command
       # self.execute_command = self.execute_command()

    def execute_command(self):
        # Load the Index JSON up to compare
        command = self.Command
        index = self.index
        arg1 = command[1]
        # Read the JSON file
        json_exist = os.path.isfile(index)
        print(json_exist)
        if json_exist == True:  # File exists so try to read it and get a value
            # Obtain details about the JSON
            with open(index) as j:
                Jsondata = json.load(j)  # Load up the Json
                try:
                    CommandDict = Jsondata['Commands']
                except KeyError:
                    print("Error: JSON has not been correctly configured")
                else:
                    # Search and see if cmd exists.
                    try:
                        Lib = CommandDict[arg1]
                    except KeyError:
                        print("Incorrect Command")
                    else:
                        # Use that library to run the command
                        print(Lib)
                        path = 'src.shell.' + Lib + '.base'
                        module = importlib.import_module(path)
                        my_class = getattr(module, 'Base')
                        instance = my_class(command)




