import re
# Q1
class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.adjacency_list[node] = []
        return node

    def removeNode(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for nodes in self.adjacency_list.values():
                if node in nodes:
                    nodes.remove(node)

    def addEdge(self, n1, n2, weight):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1].append((n2, weight))
            self.adjacency_list[n2].append((n1, weight))

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1] = [(node, weight) for node, weight in self.adjacency_list[n1] if node != n2]
            self.adjacency_list[n2] = [(node, weight) for node, weight in self.adjacency_list[n2] if node != n1]
    
    # Q2
    def importFromFile(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()

        # Check if the graph is undirected
        if not lines[0].strip() == "strict graph G {":
            return None

        # Clear existing nodes and edges
        self.adjacency_list.clear()

        # Parse edges
        for line in lines[1:-1]:
            match = re.match(r'\s*(\w+)\s*--\s*(\w+)(\s*\[weight=(\d+)\])?\s*;', line.strip())
            if match is None:
                return None

            node1_data, node2_data, _, weight = match.groups()
            weight = int(weight) if weight is not None else 1

            node1 = self.addNode(node1_data)
            node2 = self.addNode(node2_data)
            self.addEdge(node1, node2, weight)

        return self