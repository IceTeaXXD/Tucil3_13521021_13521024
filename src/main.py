from Graph import*
from AStar import*

G = Graph()
G.createGraph("test/map2.txt")
G.printGraph()
# print(G.nodes[1][0][0])
astar = AStar(1, 4, G.nodes)
astar.search()
print(astar.path)