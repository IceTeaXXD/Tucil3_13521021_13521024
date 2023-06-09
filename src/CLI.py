from Graph import*
from AStar import*
from UCS import*
from Utils import*
import time
import gmplot

G = Graph()
G.createGraph("test/map5.txt")
G.printGraph()
start = 1
goal = 11

# UCS
print("\nUNIFORM COST SEARCH")
startTime = time.perf_counter_ns()
ucs = UCS(G, start, goal)
endTime = time.perf_counter_ns()
print("Path: ", ucs.path)
print("Total Cost: ", ucs.cost)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))

# ASTAR
print("\nA STAR")
startTime = time.perf_counter_ns()
astar = AStar(start, goal, G)
endTime = time.perf_counter_ns()
print("Path: ", astar.path)
print("Total Cost: ", astar.cost)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))

G = Graph()
G.createGraphWithCoords("test/gmap2.txt")
G.printGraph()
start = 1
goal = 3
astar = AStar(start, goal, G)
print("Path: ", astar.path)
print("Total Cost: ", astar.cost, "m")

gmap = gmplot.GoogleMapPlotter(G.Maplat, G.Maplong, 17)

# give the map a title
gmap.title = G.Mapname

# give description for each node in the map
for node in G.nodes:
    gmap.marker(G.nodeID[node][1], G.nodeID[node][2], 'red', title=f"Node {node} - {G.nodeID[node][0]}.", info_window=f"Node {node} - {G.nodeID[node][0]}.")

# plot the graph, each node is a blue dot, each edge is a blue line
for node in G.nodes:
    for neighbor in G.nodes[node]:
        gmap.scatter([G.nodeID[node][1], G.nodeID[neighbor][1]], [G.nodeID[node][2], G.nodeID[neighbor][2]], 'red', size = 5, marker = False)
        gmap.plot([G.nodeID[node][1], G.nodeID[neighbor][1]], [G.nodeID[node][2], G.nodeID[neighbor][2]], 'blue', edge_width=1)

gmap.draw("result/gmap2.html")
print("Map saved to result/gmap2.html")