
class Tree:


    graph = ''
    command = ''
    def __init__(self,command):
        self.command = command
        self.createNew = self.createNew()
        if command[2] == 'create-new':
            self.graph = command[3]
            self.CreateNew()
        else:
            self.graph = command[2]
#    def createNew(self,GraphName):

    def CreateNew(self):
        name = self.graph
        # Check if graph with this name already exists
        try:
            # Open the index.json file which holds a list of installed graphs

