from Graph import*
from AStar import*
from UCS import*
from Utils import*

G = Graph()
G.createGraph("test/map4.txt")
G.printGraph()
start = 1
goal = 14


# UCS
print("\nUNIFORM COST SEARCH")
ucs = UCS(G, start, goal)
print("Path: ", ucs.path)
print("Total Cost: ", ucs.cost)

# ASTAR
print("\nA STAR")
astar = AStar(start, goal, G.nodes)
astar.search()
print("Path: ", end="")
print(astar.path)
astar.print_total_cost(astar.path, G.nodes)