# Q1
class ArrayCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("enqueue Non\n")
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
            print("dequeue None\n")
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
    def __init__(self):
        self.data = None
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
