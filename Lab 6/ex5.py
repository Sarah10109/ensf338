import random
import timeit

'''
1. Implement a class ListPriorityQueue which implements a priority queue using a linked list: [0.2 pts]
    • enqueue must insert an element in order
    • dequeue must retrieve the first (smallest) element on a list
'''

# node of the linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = ListNode(data)
        current_Data = self.head.data
        if self.head is None or data < current_Data:
            new_node.next = self.head
            self.head = new_node 
        else:
            current = self.head
            next_data = current.next.data
            while current.next is not None and next_data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue is empty. Nothing to dequeue.")
            return None
        else:
            dequeued_node = self.head
            self.head = self.head.next
            return dequeued_node.data


'''
2. Implement a class HeapPriorityQueue which implements a priority queue using a heap: [0.2 pts]
    1. Can reuse implementation from Exercise 4
'''
# from Exercise 4, we have the MinHeap class:
class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        start_index = (len(self.heap) - 2) // 2  # Start from the last non-leaf node
        for i in range(start_index, -1, -1):
            self._sift_down(i)

    def enqueue(self, element):
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        self._swap(0, len(self.heap) - 1)  # Swap the root with the last element
        min_element = self.heap.pop()  # Remove the last element (previous root)
        self._sift_down(0)  # Restore heap property
        return min_element

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._sift_up(parent_index)

    def _sift_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self._swap(index, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


'''
3. Measure execution time of both implementations [0.4 pts]
    1. Generate a random list of 1000 tasks, where a task is enqueue of a random integer with
probability 0.7, and dequeue with probability 0.3
    2. Use timeit to measure how long it takes for each implementation to process the list. Return overall time and average time per task

'''

# Q3. Write a function which generates random lists of 10000 tasks. Each
# task is either a push w/ probability 0.7, or a pop w/ probability 0.3 [0.3 pts]
def generate_tasks(n=10000):
    randomTasks = []
    for _ in range(n):
        task = 'enqueue' if random.random() < 0.7 else 'dequeue'
        randomTasks.append(task)
    return randomTasks


tasks = generate_tasks()

# Measure execution time for ListPriorityQueue
list_pq = ListPriorityQueue()
list_pq_time = timeit.timeit(lambda: [list_pq.enqueue(task[1]) if task[0] == 'enqueue' else list_pq.dequeue() for task in tasks], number=1)
print(f"ListPriorityQueue took {list_pq_time} seconds overall, {list_pq_time / len(tasks)} seconds per task")

# Measure execution time for HeapPriorityQueue
heap_pq = MinHeap()
heap_pq_time = timeit.timeit(lambda: [heap_pq.enqueue(task[1]) if task[0] == 'enqueue' else heap_pq.dequeue() for task in tasks], number=1)
print(f"HeapPriorityQueue took {heap_pq_time} seconds overall, {heap_pq_time / len(tasks)} seconds per task")



'''
4. Discuss the results: which implementation is faster? Why do you think is that?
[0.2 pts]

The heap implementation of priority queue is faster because it has logarithmic time complexity for both its inset and delete operations.



'''
