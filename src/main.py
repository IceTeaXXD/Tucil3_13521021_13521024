from Graph import*
from AStar import*
from UCS import*

G = Graph()
G.createGraph("test/map2.txt")
G.printGraph()
start = 1
goal = 8

# # ASTAR
# print("\nA STAR")
# astar = AStar(start, goal, G.nodes)
# astar.search()
# print("Path: ", end="")
# print(astar.path)
# astar.print_total_cost(astar.path, G.nodes)

# UCS
print("\nUNIFORM COST SEARCH")
ucspath = ucs(G, start, goal)
print("Path: ",end="")
print(ucspath)
print("Total cost: ",getCost(G, ucspath))