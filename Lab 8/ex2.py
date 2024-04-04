import time
import timeit
import heapq
import matplotlib.pyplot as plt


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


# parsing contents of the random.dot file to create a graph for testing
def create_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()[1:-1]  # read all lines and store in list, except the first and last line
        for line in lines:
            node_1, _, node_2, weight = line.split()
            weight = int(weight.split('=')[1][:-2])  # remove the '[weight=' and '];' part of the text, keep only the number
            # create nodes of graph
            node_1 = graph.addNode(int(node_1)) # convert the string to an int before storing
            node_2 = graph.addNode(int(node_2))
            # create the connecting edge between the two nodes
            graph.addEdge(node_1, node_2, weight)
    return graph


# function to measure performance times of slowSP
def measure_performance_slowSP(graph):
    nodes_in_graph = list(graph.adjacency_list.keys())
    max_times = [] # stores max time of every iteration (max performance time of one node) in graph 
    min_times = [] # stores min time of every iteration in graph
    avg_times = [] # stores average time of every iteration in graph
    finalTimes = [] # stores three values in the following order: overall max, overall min, and overall avg times of graph
    performance_times = [] # stores all the performance times of graph across all iterations (to be used in histogram)
    
    for node in nodes_in_graph:
        # time = timeit.timeit(lambda: graph.slowSP(node), number=10) / 10
        times = timeit.repeat(lambda: graph.slowSP(node), repeat=10, number=1)
        for time in times:
            performance_times.append(time)

        max_times.append(max(times))
        min_times.append(min(times))
        avg_times.append(sum(times)/len(times))
    
    max_time_of_graph = max(max_times)
    min_time_of_graph = min(min_times)
    avg_time_of_graph = sum(avg_times)/len(avg_times)

    finalTimes.append(max_time_of_graph)
    finalTimes.append(min_time_of_graph)
    finalTimes.append(avg_time_of_graph)

    return finalTimes, performance_times

# function to measure performance times of fastSP
def measure_performance_fastSP(graph):
    nodes_in_graph = list(graph.adjacency_list.keys())
    max_times = [] # stores max time of every iteration in graph 
    min_times = [] # stores min time of every iteration in graph
    avg_times = [] # stores average time of every iteration in graph
    finalTimes = [] # stores in order: overall max, overall min, overall avg times of graph
    performance_times = [] #stores all the performance times of graph across all iterations (to be used in histogram)
    
    
    for node in nodes_in_graph:
        times = timeit.repeat(lambda: graph.fastSP(node), repeat=10, number=1)
        for time in times:
            performance_times.append(time)

        max_times.append(max(times))
        min_times.append(min(times))
        avg_times.append(sum(times)/len(times))
    
    max_time_of_graph = max(max_times)
    min_time_of_graph = min(min_times)
    avg_time_of_graph = sum(avg_times)/len(avg_times)

    finalTimes.append(max_time_of_graph)
    finalTimes.append(min_time_of_graph)
    finalTimes.append(avg_time_of_graph)

    return finalTimes, performance_times


# test the overall timing 
graph = create_graph("random.dot") # may have to specify full file path if name alone doesn't work; adjust as needed
slowSP_times = measure_performance_slowSP(graph) 
fastSP_times = measure_performance_fastSP(graph)

print("slowSP performance times:")
print(f"max: {slowSP_times[0][0]}, min: {slowSP_times[0][1]}, average: {slowSP_times[0][2]}\n")

print("fastSP performance times:")
print(f"max: {fastSP_times[0][0]}, min: {fastSP_times[0][1]}, average: {fastSP_times[0][2]}")

# Report average, max, and min time
'''
On the first run, the max, min, and average times of both algorithms are as follows:

slowSP performance times:
max: 0.026237434999984544, min: 0.0075148449998323485, average: 0.009259502954784596

fastSP performance times:
max: 0.0012379199999941193, min: 6.047099986972171e-05, average: 6.95059247313924e-05
'''


# Q4. Plot a histogram of the distribution of execution times across all
#     nodes, and discuss the results

# Generate random data for the histogram
data_slowSP = slowSP_times[1]
data_fastSP = fastSP_times[1]
 
# Plotting a basic histogram
plt.hist(data_slowSP, bins=30, color='skyblue', edgecolor='black')
plt.hist(data_fastSP, bins=30, color='lightgreen', edgecolor='black')
 
# Adding labels and title
plt.xlabel('Execution times')
plt.ylabel('Frequency')
plt.title('Distribution of Execution Times Across all Nodes in Graph')
 
# Display the plot
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