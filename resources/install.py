class Install:

    dir = ''
    def __init__(self, dir= 'C:\\PathFinder\\'):
        self.dir = dir

    def InstallRes(self):
        """Installs all resources into the directory. From res.zip found within the package"""
