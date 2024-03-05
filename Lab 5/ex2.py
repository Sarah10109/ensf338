# Q1
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        self.queue = self.merge_sort(self.queue)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res
# Q2
class SortedPriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        # If queue is empty or data is larger than the last element, append at the end
        if not self.queue or data > self.queue[-1]:
            self.queue.append(data)
        else:
            # Find the correct spot for the data and insert it
            for i in range(len(self.queue)):
                if self.queue[i] > data:
                    self.queue.insert(i, data)
                    return

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

# Q3
import random

def generate_tasks(n=1000):
    tasks = []
    for _ in range(n):
        task = 'enqueue' if random.random() < 0.7 else 'dequeue'
        tasks.append(task)
    return tasks

# Q4
import timeit
def test_queue(QueueClass, tasks):
    queue = QueueClass()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)  # Use 1 as the data for simplicity
        else:  # task == 'dequeue'
            queue.dequeue()

task_lists = [generate_tasks() for _ in range(100)]

# PriorityQueue
def PQ():
    for tasks in task_lists:
        test_queue(PriorityQueue, tasks)

# LinkedList
def SPQ():
    for tasks in task_lists:
        test_queue(SortedPriorityQueue, tasks)

timeP = timeit.timeit(lambda: PQ(), number=1)
print(f"Time for first implementation (PriorityQueue): {timeP} seconds")

timeSP = timeit.timeit(lambda: SPQ(), number=1)
print(f"Time for second implementation (SortedPriorityQueue): {timeSP} seconds")

'''
Question 5
In the PriorityQueue class, every time an enqueue happens, the entire queue is sorted using the 
merge sort algorithm. Merge sort has a time complexity of O(nlogn), where n is the number of 
elements in the queue. So, each enqueue operation takes O(nlogn) time, making it relatively slow 
when the queue is large. In contrast, the SortedPriorityQueue class maintains a sorted queue at 
all times. When an element is enqueued, it finds the correct spot for the new element and inserts 
it there, ensuring the queue remains sorted. This operation takes O(n) time, where n is the number 
of elements in the queue. The dequeue operation is O(1) because it just removes the first element 
of the list. So, the SortedPriorityQueue class is faster because it uses a more efficient method 
to maintain the sorted order of the queue. It takes advantage of the fact that the queue is already 
sorted when inserting a new element, rather than sorting the entire queue from scratch each time. 
This results in a lower time complexity for the enqueue operation compared to the PriorityQueue 
class. 
'''