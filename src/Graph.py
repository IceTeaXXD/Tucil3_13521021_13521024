from Node import*

class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self,node):
        self.nodes[node.value] = node.neighbors

    def createGraph(self,filename):
        file = open(filename, 'r')
        i = 1
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

    def printGraph(self):
        for node in self.nodes:
            print(node, self.nodes[node])