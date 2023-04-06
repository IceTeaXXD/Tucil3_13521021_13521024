from Graph import*
from AStar import*
from UCS import*

G = Graph()
G.createGraph("test/map2.txt")
G.printGraph()
start = 1
goal = 4

# ASTAR
astar = AStar(start, goal, G.nodes)
astar.search()
print(astar.path)

# UCS
ucspath = ucs(G, start, goal)
printList(ucspath)
print(getCost(ucspath))