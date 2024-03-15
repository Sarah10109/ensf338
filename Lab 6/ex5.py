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

        if self.head == None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node 
        else:
            current_node = self.head
            while current_node.next != None and current_node.next.data < data:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def dequeue(self):
        if self.head == None:
            print("Queue is empty. Nothing to dequeue.")
            return None
        else:
            dequeued = self.head
            self.head = self.head.next
            return dequeued.data


'''
2. Implement a class HeapPriorityQueue which implements a priority queue using a heap: [0.2 pts]
    1. Can reuse implementation from Exercise 4
'''
# from Exercise 4, we have the following implementation of MinHeap:
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

# Generating a random list of 1000 tasks
def generate_tasks(n=1000):
    randomTasks = []
    for _ in range(n):
        task = 'enqueue' if random.random() < 0.7 else 'dequeue'
        randomTasks.append(task)
    return randomTasks


tasks = generate_tasks()

# Q4. Measure execution time of both implementations [0.4 pts]
def measure_execution_time(tasks, queue):
    total_time = timeit.timeit(lambda: execute_tasks(tasks, queue), number=1)
    average_time_per_task = total_time / len(tasks)
    return total_time, average_time_per_task

def execute_tasks(tasks, queue):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(random.randint(1, 100))
        else:
            try:
                queue.dequeue()
            except IndexError:
                pass  # pass if the queue is empty

# Create instances of both linked-list and heap-based priority queues
list_priorityqueue = ListPriorityQueue()
heap_priorityqueue = MinHeap()

# Measure and print time for ListPriorityQueue
total_time_list, avg_time_list = measure_execution_time(tasks, list_priorityqueue)
print(f"ListPriorityQueue - Total time: {total_time_list}, Average time per task: {avg_time_list}")

# Measure and print time for HeapPriorityQueue
total_time_heap, avg_time_heap = measure_execution_time(tasks, heap_priorityqueue)
print(f"HeapPriorityQueue - Total time: {total_time_heap}, Average time per task: {avg_time_heap}")


'''
4. Discuss the results: which implementation is faster? Why do you think is that?
[0.2 pts]

The heap implementation of priority queue is faster because it has logarithmic time complexity for both its insert and delete operations,
since our implementation of heap has a balanced tree stucture and can sift up or sift down nodes to maintain the heap properties.
On the other hand, ListPriorityQueue is slower because it takes longer to enqueue, and in the worst case scenario the program may
need to traverse the entire list in order to find the correct insertion point. 

'''
