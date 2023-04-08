from Node import*
from Utils import*

class Graph:
    def __init__(self):
        self.nodes = {}
        self.Maplat = 0
        self.Maplong = 0
        self.Mapname = ""
        self.nodeID = {}
    def addNode(self,node):
        self.nodes[node.value] = node.neighbors

    def createGraph(self,filename):
        file = open(filename, 'r')
        i = 1
        # check if the first line is 0, if not throw error
        if file.readline().split()[0] != '0':
            raise Exception("Invalid File Input!")
        for line in file:
            line = line.split()
            for j in range(0, len(line)):
                if line[j] != '0':
                    neighborValue = j+1
                    weight = float(line[j])
                    node = Node(i)
                    node.addNeighbor(neighborValue, weight)
                    if i not in self.nodes:
                        self.addNode(node)
                    else:
                        self.nodes[i][neighborValue] = weight
            i += 1

    def createGraphWithCoords(self, filename):
        file = open(filename, 'r')
        i = 1
        # the first line is the map name
        self.Mapname = file.readline().rstrip()

        # the second line is the number of nodes
        n = int(file.readline())

        # the third line is the map latitude
        self.Maplat = float(file.readline())

        # the fourth line is the map longitude
        self.Maplong = float(file.readline())

        # the next n lines are the adjacency matrix
        for i in range(n):
            line = file.readline().split()
            for j in range(0, len(line)):
                if line[j] != '0':
                    neighborValue = j+1
                    weight = float(line[j])
                    node = Node(i+1)
                    node.addNeighbor(neighborValue, weight)
                    if i+1 not in self.nodes:
                        self.addNode(node)
                    else:
                        self.nodes[i+1][neighborValue] = weight

        # the next n*3 lines are the node name, latitude, and longitude, update the node attributes
        for i in range(n):
            nama = file.readline().rstrip()
            lat = float(file.readline())
            lon = float(file.readline())
            self.nodeID[i+1] = (nama, lat, lon)

        # Edit the weight of the nodes based on the euclidean distance
        for node in self.nodes:
            for neighbor in self.nodes[node]:
                self.nodes[node][neighbor] = euclidean_distance(self.nodeID[node][1:], self.nodeID[neighbor][1:])


    def printGraph(self):
        for node in self.nodes:
            print(node, self.nodes[node])

    def printNodeID(self):
        for node in self.nodeID:
            print(node, self.nodeID[node])