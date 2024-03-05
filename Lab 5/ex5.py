# Q1
class ArrayCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("enqueue None")
            return
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
        print(f"enqueue {data}")

    def dequeue(self):
        if (self.head == -1):
            print("dequeue None")
            return
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
        print(f"dequeue {temp}")
    
    def peek(self):
        if (self.head == -1):
            print("peek None\n")
            return
        elif (self.head == self.tail):
            temp = self.queue[self.head]
        else:
            temp = self.queue[self.head]
        print(f"peek {temp}")

# Q2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LLCircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enQueue(self, data):
        new_node = Node(data) 
        if (self.front == None): 
            self.front = self.rear = new_node 
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        print(f"enqueue {data}")
    

    def deQueue(self):
        if (self.front == None):
            print("dequeue None")
            return
        if (self.front == self.rear):
            value = self.front.data
            self.front = self.rear = None
        else: 
            value = self.front.data 
            self.front = self.front.next 
            self.rear.next = self.front
        print(f"dequeue {value}")


    def peek(self):
        if (self.front == None):
            print("peek None")
            return
        print(f"peek {self.front.data}")    

# Q3
# Initialize an ArrayCircularQueue with capacity 5
print("Implementation of circular queue using an array of size 5:")
array_queue = ArrayCircularQueue(5)

# Enqueue some elements
array_queue.enqueue(1)  # Expected output: "enqueue 1"
array_queue.enqueue(2)  # Expected output: "enqueue 2"
array_queue.enqueue(3)  # Expected output: "enqueue 3"
array_queue.peek()      # Expected output: "peek 1"
array_queue.enqueue(4)  # Expected output: "enqueue 4"
array_queue.enqueue(5)  # Expected output: "enqueue 5"

# Try to enqueue into a full queue
array_queue.enqueue(6)  # Expected output: "enqueue None"

# Dequeue some elements
array_queue.dequeue()  # Expected output: "dequeue 1"
array_queue.peek()      # Expected output: "peek 2"
array_queue.dequeue()  # Expected output: "dequeue 2"
array_queue.dequeue()  # Expected output: "dequeue 3"
array_queue.dequeue()  # Expected output: "dequeue 4"
array_queue.dequeue()  # Expected output: "dequeue 5"

# Try to dequeue from an empty queue
array_queue.dequeue()  # Expected output: "dequeue None"

# Try to peek at an empty queue
array_queue.peek()  # Expected output: "peek None"

# Initialize an LLCircularQueue
print("Implementation of circular queue using a linked list:")

linked_list_queue = LLCircularQueue()

# Enqueue some elements
linked_list_queue.enQueue(1)  # Expected output: "enqueue 1"
linked_list_queue.enQueue(2)  # Expected output: "enqueue 2"
linked_list_queue.enQueue(3)  # Expected output: "enqueue 3"
linked_list_queue.peek()      # Expected output: "peek 1"
linked_list_queue.enQueue(4)  # Expected output: "enqueue 4"
linked_list_queue.enQueue(5)  # Expected output: "enqueue 5"

# Dequeue some elements
linked_list_queue.deQueue()  # Expected output: "dequeue 1"
linked_list_queue.deQueue()  # Expected output: "dequeue 2"
linked_list_queue.peek()      # Expected output: "peek 3"
linked_list_queue.deQueue()  # Expected output: "dequeue 3"
linked_list_queue.deQueue()  # Expected output: "dequeue 4"
linked_list_queue.deQueue()  # Expected output: "dequeue 5"

# Try to dequeue from an empty queue
linked_list_queue.deQueue()  # Expected output: "dequeue None"

# Try to peek at an empty queue
linked_list_queue.peek()  # Expected output: "peek None"

# Enqueue more elements
linked_list_queue.enQueue(6)  # Expected output: "enqueue 6"
linked_list_queue.peek()      # Expected output: "peek 6"
linked_list_queue.enQueue(7)  # Expected output: "enqueue 7"
linked_list_queue.enQueue(8)  # Expected output: "enqueue 8"
linked_list_queue.enQueue(9)  # Expected output: "enqueue 9"

# Dequeue some elements
linked_list_queue.deQueue()  # Expected output: "dequeue 6"
linked_list_queue.deQueue()  # Expected output: "dequeue 7"
linked_list_queue.deQueue()  # Expected output: "dequeue 8"
linked_list_queue.peek()      # Expected output: "peek 9"
linked_list_queue.deQueue()  # Expected output: "dequeue 9"

# Try to dequeue from an empty queue
linked_list_queue.deQueue()  # Expected output: "dequeue None"

# Try to peek at an empty queue
linked_list_queue.peek()  # Expected output: "peek None"