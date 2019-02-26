import src.shell.builder
class Base:

    # Base Class
    command = ''
    def __init__(self,command):
        self.command = command
        self.ProcessCommand()

    def ProcessCommand(self):
        # This procedure will internally process the command to the right file.
        command = self.command
        src.shell.builder.tree.Tree(command)
