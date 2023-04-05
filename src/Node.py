class Node:
    def __init__(self, value):
        self.value = value
        self.edges = {}
        # key : value neighbor
        # value : weight nya
        
    def addEdge(self, node, weight):
        self.edges[node] = weight
    
    def getEdges(self):
        return self.edges
    
    def getValue(self):
        return self.value    
