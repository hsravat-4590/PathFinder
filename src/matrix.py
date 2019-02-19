import os.path
import json


class Matrix:

    # Matrix Class is used to handle raw node data and parse it into a Json File for Dijkstra
    graph = {}  # Matrix holds graph
    NodeArray = [] # Array with all nodes of the network
    JsonFile = "data.json"  # Link to Json File (Set as a blank string)
    JSON = 0
    Meta_JSON = {}
    JSON_KEYS = ["JSON_TYPE","GRAPH_NAME","NODES","NODE_ARRAY","NODE_CONNECTIONS","CONNECTION_DISTANCES"]

    def CheckJson(doall=True,Meta_JSON=Meta_JSON,SaveRAM = False,Get_JsonType = False,GetNodes = False,GetNodeArray = False,GetConnections=False,GetDistances= False):
        """Saves all Get Properties in Meta_JSON Dict. If only one Get is True, Then the value will be returned."""
        if doall== True:
            SaveRAM = True
            GetDistances = True
            GetConnections = True
            GetNodeArray = True
            GetNodes = True
            Get_JsonType = True
        global JsonFile
        JsonFile = "data.json"
        # global Meta_JSON
        json_exist = os.path.isfile("data.json")
        if json_exist == True :  # File exists so try to read it and get a value
            # Obtain details about the JSON
            with open(JsonFile) as j:
                Jsondata = json.load(j) # Load up the Json
                if SaveRAM == True:
                    # Save Contents of JSON into Memory
                    global JSON
                    JSON = Jsondata  # Save the JSON DATA (RAW to Memory)
                if Get_JsonType == True:
                    try:
                        a = Jsondata["JSON_TYPE"]
                    except KeyError:
                        print("Error: JSON Not Correctly configured")
                        return "JSONCFGINOP"
                    else:
                        Meta_JSON["Type"] = Jsondata["JSON_TYPE"]
                if GetNodes == True:
                    try:
                        a = Jsondata["NODES"]
                    except KeyError:
                        print("Error: JSON Not Correctly configured")
                        return "JSONCFGINOP"
                    else:
                        Meta_JSON["NodeNo"] = Jsondata["NODES"]
                if GetNodeArray == True:
                    try:
                        a = Jsondata["NODE_ARRAY"]
                    except KeyError:
                        print("Error: JSON Not Correctly configured")
                        return "JSONCFGINOP"
                    else:
                        Meta_JSON["NodeLi"] = Jsondata["NODE_ARRAY"]
                if GetConnections == True:
                    try:
                        a = Jsondata["NODE_CONNECTIONS"]
                    except KeyError:
                        print("Error: JSON Not Correctly configured")
                        return "JSONCFGINOP"
                    else:
                        Meta_JSON["NodeConn"] = Jsondata["NODE_CONNECTIONS"]
                if GetDistances == True:
                    try:
                        a = Jsondata["CONNECTION_DISTANCES"]
                    except KeyError:
                        print("Error: JSON Not Correctly configured")
                        return "JSONCFGINOP"
                    else:
                        Meta_JSON["NodeDist"] = Jsondata["CONNECTION_DISTANCES"]
            return "JSONEXIST"
        else:
            return "NULLEXIST"

    def PopulateRegisters(send = True):
        '''This Command can be used to populate the matrix registers with JSON data.'''

        # Check JSON and save a RAW Version.
        Matrix.CheckJson(True)
        global Meta_JSON
        return Meta_JSON

    def GetJsonData(SpecificDataType = 0):  # Returns The JSON as a String unless the dev specifically requests a key.
        if SpecificDataType == 0 :
            # Just Return the JSON.
            File = Matrix.JsonFile
            if os.path.exists(File):
                with open(File, 'rb') as f:
                    try:
                        # File Exists. Do something!
                        Jsondata = json.load(f)  # Load up the Json
                        return Jsondata
                    except:  # whatever reader errors you care about
                # handle error
                        print("Error File Does not exist")
                        return "I/O Error"
        elif SpecificDataType != 0:
            # Does Not Equal Zero.
            try:
                key = Matrix.JSON_KEYS.index(SpecificDataType)
            except ValueError:
                # Isn't a configured Key
                print("Incorrect Key")
                return("KEYINOP")
            else:
                File = Matrix.JsonFile
                if os.path.exists(File):
                    with open(File, 'rb') as f:
                        try:
                            # File Exists. Do something!
                            Jsondata = json.load(f)  # Load up the Json
                            try:
                                retkey=Jsondata[SpecificDataType]
                            except KeyError:
                                print("JSONCFGERR")
                            else:
                                return Jsondata[SpecificDataType]
                        except:  # whatever reader errors you care about
                            # handle error
                            print("Error File Does not exist")
                            return "I/O Error"