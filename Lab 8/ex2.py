import time
import timeit
import heapq
import matplotlib.pyplot as plt
import re


# Q1. List two possible ways to implemenent queue for finding a node in 
#     the algorithm


'''
Two possible ways to implement the queue:
    1. Array implementation, done via linear search, which is inefficient 
    2. Priority queue implementation using a heap, which is an efficient implementation
'''



# Q2. Implement two version of the algorithm, one with the inefficient
#     node selection logic, and one with the efficient node selection logic.

# note: the Graph class from ex1 was used here. The fastSP and slowSP functions are defined within the class
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
    # Algorithms for calculating minimum distance between nodes
    def slowSP(self, source):
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[source] = 0

        queue = list(self.adjacency_list.keys())
        while queue:
            min_node = min(queue, key=lambda node: distances[node])
            queue.remove(min_node)

            for neighbor_node, weight in self.adjacency_list[min_node]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor_node]:
                    distances[neighbor_node] = new_distance

        return distances

    def fastSP(self, source):
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[source] = 0

        queue = [(0, source)]
        while queue:
            current_distance, min_node = heapq.heappop(queue)

            if current_distance > distances[min_node]:
                continue

            for neighbor_node, weight in self.adjacency_list[min_node]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor_node]:
                    distances[neighbor_node] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor_node))

        return distances


# Q3. Measure the performance of each algorithm on the sample graph
#     provided on the lab’s D2L (random.dot). [0.2 pts]
#       • Time the execution of the algorithm, for all nodes
#       • Report average, max and min time

# Initialize the Graph
g = Graph()
g.importFromFile("random.dot")

# Initialize the lists to store the execution times
slow_times = []
fast_times = []

# Get a subset of the nodes
nodes_subset = list(g.adjacency_list.keys())[:100]  # Adjust this value based on your needs

# Measure the execution time of each algorithm for each node in the subset
for node in nodes_subset:
    # Measure the execution time of slowSP(node)
    start_time = timeit.default_timer()
    g.slowSP(node)
    end_time = timeit.default_timer()
    slow_times.append(end_time - start_time)

    # Measure the execution time of fastSP(node)
    start_time = timeit.default_timer()
    g.fastSP(node)
    end_time = timeit.default_timer()
    fast_times.append(end_time - start_time)

# Calculate the average, max, and min time for each algorithm
slow_avg = sum(slow_times) / len(slow_times)
slow_max = max(slow_times)
slow_min = min(slow_times)

fast_avg = sum(fast_times) / len(fast_times)
fast_max = max(fast_times)
fast_min = min(fast_times)

# Print the results
print(f"slowSP(node): avg = {slow_avg}, max = {slow_max}, min = {slow_min}")
print(f"fastSP(node): avg = {fast_avg}, max = {fast_max}, min = {fast_min}")

# Plot the histogram for slowSP(node)
plt.figure(figsize=(10, 5))
plt.hist(slow_times, bins=30, alpha=0.5, color='r', label='slowSP(node)', edgecolor='black')
plt.xlabel('Execution Time')
plt.ylabel('Frequency')
plt.title('Histogram of Execution Times for slowSP(node)')
plt.legend()
plt.show()

# Plot the histogram for fastSP(node)
plt.figure(figsize=(10, 5))
plt.hist(fast_times, bins=30, alpha=0.5, color='b', label='fastSP(node)', edgecolor='black')
plt.xlabel('Execution Time')
plt.ylabel('Frequency')
plt.title('Distribution of Execution Times Across all Nodes in Graph')
plt.legend()
plt.show()

'''
Discussion of timing results:

Overall, the execution time of fastSP is faster than that of slowSP. This is because
fastSP is implemented with a heap-based priority queue, which stores the node with the smallest 
distance at the top, and extracting this node can be acheieved in O(log(n)) time. On the other hand,
slowSP uses linear search and traverses through all nodes in the queue until the one with the smallest
distance is found. To extract the node with the smallest distance using this method takes O(n) time, which
is much less efficient than fastSP.

'''