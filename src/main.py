from Graph import*
from AStar import*
from UCS import*
from Utils import*

G = Graph()
G.createGraph("test/map2.txt")
G.printGraph()
start = 1
goal = 3


# UCS
print("\nUNIFORM COST SEARCH")
ucs = UCS(G, start, goal)
print("Path: ", ucs.path)
print("Total Cost: ", ucs.cost)

# ASTAR
print("\nA STAR")
astar = AStar(start, goal, G.nodes)
print("Path: ", astar.path)
print("Total Cost: ", astar.cost)