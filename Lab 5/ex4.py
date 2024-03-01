# Q1
class ArrayQueue:
    def __init__(self, c):
        self.queue = []
        self.capacity = c
 
    def enqueue(self, data): 
        if(len(self.queue) == self.capacity):
            return
        else:
            self.queue.insert(0, data)
 
    # Function to delete an element
    # from the front of the queue
    def dequeue(self):
        if(len(self.queue) == 0):
            return
        else:
            x = self.queue.pop()
            return x

# Q2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is not None:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node

    def dequeue(self):
        if self.isEmpty():
            return 
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        return data
    
# Q3
import random

def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        task = 'enqueue' if random.random() < 0.7 else 'dequeue'
        tasks.append(task)
    return tasks
 
# Q4
import timeit
def test_queue(QueueClass, tasks):
    queue = QueueClass(10000) if QueueClass.__name__ == 'ArrayQueue' else QueueClass()
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)  # Use 1 as the data for simplicity
        else:  # task == 'dequeue'
            queue.dequeue()

task_lists = [generate_tasks() for _ in range(100)]

# ArrayQueue
def arrQ():
    for tasks in task_lists:
        test_queue(ArrayQueue, tasks)

# LinkedList
def LLQ():
    for tasks in task_lists:
        test_queue(Queue, tasks)

timeArr = timeit.timeit(lambda: arrQ(), number=1)
print(f"Time for first implementation (ArrayQueue): {timeArr} seconds")

timeLL = timeit.timeit(lambda: LLQ(), number=1)
print(f"Time for second implementation (Queue): {timeLL} seconds")

# Q5
import matplotlib.pyplot as plt
timeArr = [timeit.timeit(lambda: test_queue(ArrayQueue, tasks), number=1) for tasks in task_lists]
timeLL = [timeit.timeit(lambda: test_queue(Queue, tasks), number=1) for tasks in task_lists]


plt.hist(timeArr, color='skyblue', edgecolor='black', label='Array Queue')
plt.hist(timeLL, color='green', edgecolor='black', alpha=0.5, label='Linked List Queue')
plt.xlabel('Time Taken')
plt.ylabel('Frequency')
plt.title('Measurements of Different Implementation')
plt.legend()
plt.show()

'''
The time taken for the linked list queue is much longer then the array queue. That is because the 
linked list queue when it dequeues it needs to iterate through the linked list to eventually dequeue
the last item. And since the enqueue has a higher chance of occurrence, the linked list would be big 
because the dequeuing doesn't occur as much.
'''