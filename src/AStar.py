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
        self.open = []
        self.closed = []
        self.path = []
        self.init_node(self.start)
        
    def init_node(self, node):
        node.g = 0
        node.h = self.get_heuristic(node)
        node.f = node.g + node.h
        node.parent = None

    def get_heuristic(self, node):
        return abs(node.value - self.goal.value)

    def get_adjacent_nodes(self, node):
        nodes = []
        for n in self.graph[node.value]:
            adj_node = Node(n[0])
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
        for n in self.graph[node.value]:
            if n[0] == adj.value:
                adj.g = node.g + n[1]
        adj.h = self.get_heuristic(adj)
        adj.f = adj.g + adj.h
        adj.parent = node

    def search(self):
        self.open.append(self.start)
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
                if adj_node in self.closed:
                    continue
                if adj_node in self.open:
                    for n in self.graph[node.value]:
                        if n[0] == adj_node.value:
                            if adj_node.g > node.g + n[1]:
                                self.update_node(adj_node, node)
                else:
                    print(adj_node.value)
                    print(node.value)
                    self.update_node(adj_node, node)
                    self.open.append(adj_node)
        return None
