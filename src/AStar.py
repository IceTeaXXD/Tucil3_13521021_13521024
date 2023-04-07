class Node:
    def __init__(self, value):
        self.value = value
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

class AStar:
    def __init__(self, start, goal, graph):
        self.start = Node(start)
        self.goal = Node(goal)
        self.graph = graph
        self.open = [self.start]
        self.closed = []
        self.path = []
        self.init_node(self.start)
        
    def init_node(self, node):
        node.g = 0
        node.h = self.get_heuristic(node)
        node.f = node.g + node.h
        node.parent = None

    def get_heuristic(self, node):
        return 0

    def get_adjacent_nodes(self, node):
        nodes = []
        for n in self.graph[node.value]:
            adj_node = Node(n)
            self.init_node(adj_node)
            nodes.append(adj_node)
        return nodes

    def get_lowest_f(self):
        lowest = None
        for node in self.open:
            if lowest is None or node.f < lowest.f:
                lowest = node
        return lowest

    def get_path(self):
        while node is not None:
            self.path.append(node.value)
            node = node.parent
        self.path.reverse()

    def update_node(self, adj, node):
        adj.g = node.g + self.graph[node.value][adj.value]
        adj.h = self.get_heuristic(adj)
        adj.f = adj.g + adj.h
        adj.parent = node

    def search(self):
        while len(self.open) > 0:
            node = self.get_lowest_f()
            self.open.remove(node)
            self.closed.append(node)
            if node.value == self.goal.value:
                while node is not None:
                    self.path.append(node.value)
                    node = node.parent
                self.path.reverse()
                return self.path
            adj_nodes = self.get_adjacent_nodes(node)
            for adj_node in adj_nodes:
                if adj_node.value in [n.value for n in self.closed]:
                    continue
                if adj_node.value in [n.value for n in self.open]:
                    if adj_node.g > node.g + self.graph[node.value][adj_node.value]:
                        self.update_node(adj_node, node)
                        continue
                self.open.append(adj_node)
                self.update_node(adj_node, node)
        return None

    def print_total_cost(self, path, graph):
        total_cost = 0
        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i+1]
            for neighbor in graph[node1]:
                if neighbor == node2:
                    total_cost += graph[node1][neighbor]
        print("Total cost:", total_cost)