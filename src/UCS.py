from Graph import*
from queue import PriorityQueue

class UCS:
    def __init__(self, graph: Graph, startNode: int, goalNode: int) -> None:
        self.graph = graph
        self.startNode = startNode
        self.goalNode = goalNode
        self.path = self.ucs()
        self.cost = self.getCost(self.path)

    def getCost(self,path) -> int:
        if path is None:
            return -1
        cost = 0
        for i in range(len(path)-1):
            cost += self.graph.nodes[path[i]][path[i+1]]
        return cost

    def ucs(self) -> list:
        # Variables Initialization
        pq = PriorityQueue()
        pq.put((0, [self.startNode]))
        
        while pq.qsize() > 0:
            # Get the first element from the list
            pathTemp = pq.get()[1]

            # Get the last node from the path
            lastNode = pathTemp[len(pathTemp)-1]

            # Check if the last node is the goal node
            if lastNode == self.goalNode:
                return pathTemp
            
            # if the last node in the path is not the goal, enqueue all the neighbors of the last node
            for neighbor in self.graph.nodes[lastNode]:
                # if the neighbor is not in the path, enqueue it
                if neighbor not in pathTemp:
                    # create a new path
                    pathNew = []

                    # copy the path to the new path
                    for i in range(len(pathTemp)):
                        pathNew.append(pathTemp[i])

                    # enqueue the neighbor to the new path
                    pathNew.append(neighbor)

                    # enqueue the new path to the list based on the total cost
                    total = self.getCost(pathNew)
                    pq.put((total, pathNew))

        return None