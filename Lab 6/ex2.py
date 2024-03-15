# Q1
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data <= current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, current_node):
        if current_node is None:
            return None
        elif data == current_node.data:
            return current_node
        elif data < current_node.data:
            return self._search(data, current_node.left)
        else:
            return self._search(data, current_node.right)

def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Q2
import timeit
import random

# Assuming Node and BinarySearchTree classes are defined as per the previous instructions

def generate_and_build_tree(n=10000):
    # Generate a sorted vector
    sorted_vector = list(range(n))
    # Shuffle the vector
    shuffled_vector = sorted_vector[:]
    random.shuffle(shuffled_vector)

    # Build a BST by inserting each element from the shuffled vector
    bst = BinarySearchTree()
    for element in shuffled_vector:
        bst.insert(element)

    return bst, shuffled_vector  # Return both bst and shuffled_vector


def measure_search_performance(bst, sorted_vector):
    total_time = 0

    # Function to be timed for each element
    def search_element(bst, element):
        bst.search(element)

    # Measure search time for each element, averaged over 10 tries
    for element in sorted_vector:
        time = timeit.timeit(lambda: search_element(bst, element), number=10) / 10
        total_time += time

    # Calculate average time
    average_time = total_time / len(sorted_vector)

    return average_time, total_time

# Generate and build the BST
bst, shuffled_vector = generate_and_build_tree()

# Measure search performance
average_time, total_time = measure_search_performance(bst, shuffled_vector)
print("Time using a binary search tree")
print(f"Average search time per element: {average_time} seconds")
print(f"Total search time for all elements: {total_time} seconds")

# Q3
# Assuming the binary_search function is defined as per previous instructions

def sort_vector(shuffled_vector):
    # Sort the shuffled vector
    sorted_vector = sorted(shuffled_vector)
    return sorted_vector

def measure_binary_search_performance(sorted_vector):
    total_time = 0

    # Function to be timed for each element
    def binary_search_element(sorted_vector, element):
        binary_search(sorted_vector, element)

    # Measure search time for each element, averaged over 10 tries
    for element in sorted_vector:
        time = timeit.timeit(lambda: binary_search_element(sorted_vector, element), number=10) / 10
        total_time += time

    # Calculate average time
    average_time = total_time / len(sorted_vector)

    return average_time, total_time


# Now use the shuffled_vector for binary search performance measurement
sorted_vector = sort_vector(shuffled_vector)  # Sort the shuffled vector
average_time, total_time = measure_binary_search_performance(sorted_vector)
print("Time using binary search in an array")
print(f"Average binary search time per element: {average_time} seconds")
print(f"Total binary search time for all elements: {total_time} seconds")

'''
Q4
"Binary search in a sorted array typically outperforms searching in a binary search tree (BST) due to its 
efficient memory usage and consistent O(log n) search time in both average and worst-case scenarios. This efficiency 
is partly due to the array's contiguous memory layout, which optimizes CPU cache utilization. In contrast, a BST's 
search efficiency can vary; while it also achieves O(logn) in average cases, particularly for balanced trees, 
it can deteriorate to O(n) in the worst-case scenario when the tree becomes highly unbalanced, resembling a linear 
structure. This variance makes BSTs less predictable in terms of performance, especially for large datasets.
'''