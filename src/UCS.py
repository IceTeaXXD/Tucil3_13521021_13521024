from Graph import*

def list_to_adjacent_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

def resultToArray(res):
    arr = []
    for i in range(len(res)):
        arr.append(res[i][1])
    return arr

def printList(arr):
    if arr is None:
        print("No path found")
        return
    for i in range(len(arr)):
        print(arr[i][1], end=" ")
    print()

def getCost(arr):
    if arr is None:
        return -1
    cost = 0
    for i in range(len(arr)):
        cost += arr[i][0]
    return cost

def notElmt(val, arr):
    for i in range(len(arr)):
        if arr[i][1] == val:
            return False
    return True

def ucs(graph, startNode, goalNode):
    # Variables Initialization
    arr = [] # list of priority queues
    temp = [(0,startNode)]
    arr.append(temp)
    while len(arr) > 0:
        # Pop the first element from the list
        pathTemp =  arr.pop(0)

        # Get the last node from the path
        lastNode = pathTemp[len(pathTemp)-1]

        # Check if the last node is the goal node, if yes return the path
        if lastNode[1] == goalNode:
            return pathTemp

        # if the last node in the path is not the goal, enqueue all the neighbors of the last node
        for neighbor in graph.nodes[lastNode[1]]:
            # if the neighbor is not in the path, enqueue it
            if notElmt(neighbor[0], pathTemp):
                # create a new path
                pathNew = []

                # copy the path to the new path
                for i in range(len(pathTemp)):
                    pathNew.append(pathTemp[i])

                # enqueue the neighbor to the new path
                pathNew.append((neighbor[1], neighbor[0]))

                # enqueue the new path to the list based on the total cost
                total = getCost(pathNew)

                if len(arr) == 0:
                    arr.append(pathNew)
                else:
                    for i in range(len(arr)):
                        if total < getCost(arr[i]):
                            arr.insert(i, pathNew)
                            break
                        elif i == len(arr)-1:
                            arr.append(pathNew)
                            break
    return None