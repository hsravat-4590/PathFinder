class GetSet:
    # class to get info of objects stored in res

    variable = 'dud'
    InFile = 'none'

    def __init__(self, variable, InFile = 'nothing'):
        self.variable = variable
        self.InFile = InFile
        self.Index = self.Index()

    class Index:

        def Get(self, variable, InFile = 'nothing'):
            # Get an Index
            if InFile == 'nothing':
                # No additional data has been provided so we need to search all files for this variable
                # Open res index for folder struct.


        def Set(self, variable):
            # Set an Index Property

        def CacheIndexes(self):
            # Cache the indexes for faster search operations