'''
Q1
Topological sorting can be implemented using the Depth-Frist Search (DFS) algorithm.
The DFS-based algorithm for topological sorting works as follows:
1) It calls DFS for the graph to get the finish time of each vertex.
2) Store the vertices in decreasing order of their finish time. This gives us the topological sorting of the graph.
The reason DFS is used for topological sorting is because it explores as far as possible along each branch before backtracking, 
which is suitable for scheduling problems represented by directed acyclic graphs (DAGs). In such problems, certain tasks must be 
performed before others, and DFS helps in identifying these dependencies.
'''

import re

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
    
    # Q2
    def isdag(self):
        visited = set()
        path = set()

        for node in self.adjacency_list:
            if node not in visited:
                if self._has_cycle(node, visited, path):
                    return False
        return True

    def _has_cycle(self, node, visited, path):
        visited.add(node)
        path.add(node)

        for neighbor, _ in self.adjacency_list[node]:
            if neighbor not in visited:
                if self._has_cycle(neighbor, visited, path):
                    return True
            elif neighbor in path:
                return True

        path.remove(node)
        return False
    
    def toposort(self):
        # Check if the graph is a DAG
        if not self.isdag():
            return None

        visited = set()
        stack = []

        # Define the DFS function
        def dfs(node):
            visited.add(node)
            for neighbour, _ in self.adjacency_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            stack.insert(0, node)

        # Perform DFS for each unvisited node
        for node in self.adjacency_list:
            if node not in visited:
                dfs(node)

        # Return the nodes in topological order
        return stack
    
    # Q3
    def toposort(self):
        if not self.isdag():
            return None

        visited = set()
        stack = []

        for node in self.adjacency_list:
            if node not in visited:
                self._dfs(node, visited, stack)

        return [node.data for node in stack[::-1]]  # reverse the list before returning

    def _dfs(self, node, visited, stack):
        visited.add(node)

        for neighbor, _ in self.adjacency_list[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)

        stack.append(node)