from Node import*

class Graph:
    def __init__(self):
        self.nodes = []
    
    def addNodes(self, nodes):
        self.nodes.append(nodes)

    # Read Adjacency List from file
    def readAdjacencyList(self, filename):
        file = open(filename, 'r')
        i = 1
        for line in file:
            line = line.split()
            self.addNodes(Node(i))
            for j in range(0, len(line)):
                # if (i != j+1): # skip self node
                    neighborValue = j+1
                    weight = float(line[j])
                    self.nodes[i-1].addEdge(neighborValue, weight)
            i += 1

    def printNodes(self):
        for node in self.nodes:
            print (node.getValue(), node.getEdges())