class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []    
    
    def addNeighbor(self,neighborValue,weight):
        self.neighbors.append((neighborValue,weight))