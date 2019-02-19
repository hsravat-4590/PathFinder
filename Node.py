import math
import random


# Node Class

# Get NodeArray and plot Coord

__nodeArray = []
__x_cords = {}
__y_cords = {}
distanceMatrix = {}
djikstraDistance = {}
connectionMatrix = {}
addcount=0
count = 0 # counter
visitedNodes = {}
NodeDat = []
build = False
CONNECTION_FOUND = False  # Working with NodeArray to build a graph
TreeBranch=[]
Found = False
currentDistance = 0
NearestConnection = ""
NearestConnectionDistance = 0
route =[]
shortestVertex = 0

# GetSet lambda
__connectionArray__= lambda node: connectionMatrix[node]

def buildDict():
    """Builds all dicts from stored nodes"""
    # Turn on Build Mode
    build = True
    # Add all nodes from NodeDat
    for node in NodeDat:
        addItem(node)
        # Build the VisitedNode Dictionary and set to false
        visitedNodes[node] = False
    # Find all distances after that is done and build distance matrix
    findDistance()
    # Build the VisitedNode Dictionary


def addItem(Node):
    """Nodes are formatted as follows: ["<name>",<x-cord>,<y-cord>,<[Connects To]>]"""
    try:
        NodeDat.index(Node)
    except ValueError:
        if build == True:
            pass
        else:
            NodeDat.append(Node)
    else:
        pass

    # Check if node already exists
    nodename = Node[0]
    #print(nodename)

    try:
        __nodeArray.index(nodename)
    except ValueError:
        # New Item
        __nodeArray.append(nodename)
        # Save coords in dicts
        __x_cords[nodename] = Node[1]
        __y_cords[nodename] = Node[2]
        # Check if node already exists in matrix
        connectionMatrix[nodename] = Node[3]  # Add the Connected Nodes to the Connection matrix
        DctConnections = Node[3]
        for node in DctConnections:
            if node in connectionMatrix:
                L1 = connectionMatrix[node]
                # Check if the Connection has already been written otherwise include in Key
                try:
                    L1.index(nodename)
                except ValueError:
                    L1.append(nodename)
                else:
                    pass # Nothing needs to happen
    else:
        __updateItem(Node)


def __updateItem(Node): #
    """Nodes are formatted as follows: ["<name>",<x-cord>,<y-cord>,<[Connects To]>]"""

    # update Co-ordinates
    __x_cords[Node[0]] = Node[1]
    __y_cords[Node[0]] = Node[2]
    nodename = Node[0]
    # working with connections now
    DctConnections = Node[3]
    for node in DctConnections:
        if node in connectionMatrix:
            L1 = connectionMatrix[node]
            # Check if the Connection has already been written otherwise include in Key
            try:
                L1.index(nodename)
            except ValueError:
                L1.append(nodename)
            else:
                pass  # Nothing needs to happen


def findDistance(): # Builds a distance matrix (all of the connections)
    # Find the distances between nodes that connect
    NodeList = __nodeArray
    TreeSize=len(NodeList)
    for node in NodeList:
        # Work through the nodelist
        # Check in Connection matrix to find which items the node connects to
        NodeConnections=connectionMatrix[node]
        for connection in NodeConnections:
            # Find the distance between the two points and save in dictionary
            x_cords=__x_cords
            y_cords=__y_cords
            nodeX = x_cords[node]
            nodeY = y_cords[node]
            connectionX = x_cords[connection]
            connectionY = y_cords[connection]
            dy = nodeY-connectionY
            dx = nodeX-connectionX
            if dy == 0 and dx != 0:
                distance = dx
            elif dx == 0 and dy != 0:
                distance = dy
            elif dx == 0 and dy == 0:
                distance = 0
            else:
                distance = math.hypot(dx,dy) # Find the straight line distance
            name = node+connection
            distanceMatrix[name] = distance


def checkConnect(StartNode, DestNode):
    """This Function can be used to see if two nodes are connected returns bool, arg1 can be array or string"""
    # Find out what type <startNode> is
    if type(StartNode) == list:
        for node in StartNode:
            print(node)
            if node == DestNode:
                TreeBranch.clear()

                return True
            else:
                    NodeConnections = connectionMatrix[node]
                    try:
                        NodeConnections.index(DestNode)
                    except ValueError:
                        # Get All of its connections and store it in an Array (TreeBranch)
                        TreeBranch.extend(__connectionArray__(node))
                        print(TreeBranch)
                        Found = False
                        continue
                    else:
                        TreeBranch.clear()
                        return True
        if Found == False:
            checkConnect(TreeBranch, DestNode)
    elif type(StartNode) == str:
        # Send in as list
        li = [StartNode]
        checkConnect(li,DestNode)

    else:
        raise ValueError("Error: [StartNode] is not a list or string")


def Djikstra(StartNode, DestNode):
    """Find the shortest Path between two nodes on a network"""
    # Check if a route is possible
    # Run Build to ensure that all nodes, connections and distances are up to date
    buildDict()
    topNode = StartNode  # Node at base
    if checkConnect(StartNode, DestNode) is True:
        # A route is possible Continue
        # Mark StartNode distance as 0
        djikstraDistance[StartNode] = 0
        # Find the nearest Connection
        connectors = connectionMatrix[StartNode]
        for x in connectors:
            nodeDist = distanceMatrix[x+topNode]
            if visitedNodes[x] is True:
                continue
            else:
                visitedNodes[x] = True
                if shortestVertex is 0:
                    # set connection distance as shortest vertex
                    shortestVertex = nodeDist
                    topNode = x
                elif shortestVertex >= nodeDist:
                    shortestVertex = nodeDist
                    topNode = x
                else:
                    continue  # current vetex is shorter
        # 

    else:
        # A route is not possible
        raise ValueError("Error in checkConnect while checking if Node: " + StartNode+" can connect to: " + DestNode + ". No route is possible")


# Populate Dicts and Arrays
addItem(['f', 12, 11, ['l', 't', 'j']])
addItem(['d', 9, 4, ['e', 'u', 'y']])
addItem(['t', 7, 1, ['e', 'u', 'c']])
addItem(['l', 2, 11, ['d', 'n', 'c']])
addItem(['j', 20, 11, ['t', 'u', 'f']])
addItem(['y', 20, 7, ['f', 'l', 'j']])
addItem(['u', 16, 3, ['l', 't', 'f']])
addItem(['a', 13, 19, ['t', 'l', 'n']])
addItem(['c', 18, 16, ['l', 'd', 'f']])
addItem(['n', 9, 18, ['t', 'y', 'a']])
addItem(['e', 11, 14, ['y', 'n', 'j']])
buildDict()
print(visitedNodes)
findDistance()
print(distanceMatrix)
