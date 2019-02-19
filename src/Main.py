import src
import json
matrix = src.Matrix
visitednodes = []
nodeConnections = {}
connectionDistances = {}
DjikstraMatrix = {}

def __main__(StartNode,EndNode):
    """Finds the shortest distance between the two nodes"""
    print("Loading JSON File...")
    JSONData = matrix.GetJsonData()
    print("Done")
    print("Got JSON DATA:", JSONData)
    print("loading JSON")
    nodeConnections = matrix.GetJsonData("NODE_CONNECTIONS")
    print(nodeConnections)
    connectionDistances = matrix.GetJsonData("CONNECTION_DISTANCES")
    print(nodeConnections)
    print(connectionDistances)
    ##Djikstra Starts Here.
    WorkingNode = StartNode
    DjikstraMatrix[WorkingNode] = [1,0]
    visitednodes.append(WorkingNode)
    print(DjikstraMatrix)
    while True:
        # Find the Shortest Connection.
        ThisNodeConnections = nodeConnections[WorkingNode]
        # ThisNodeConnectionDistances = connectionDistances[WorkingNode]
        for i in ThisNodeConnections:
            # Work through the connections
            print(i)

__main__('S','T')

