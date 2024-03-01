import timeit
import random

'''
In this exercise you will analyze the performance of different stack
implementations

1. Implement a stack which internally uses Python arrays. push() must
append an element at the tail, and pop() must remove an element
from the tail [0.3 pts]

2. Implement a stack which internally uses a singly-linked list. push()
must add an element at the head, and pop() must remove the head
element [0.3 pts]

3. Write a function which generates random lists of 10000 tasks. Each
task is either a push w/ probability 0.7, or a pop w/ probability 0.3
[0.3 pts]

4. Measure the performance of both implementations on 100 such
lists of tasks using timeit and print the results [0.3 pts]

5. Plot the distribution of times (distributions for each implementation
should be overlayed in the same plot; make sure to use consistent
ranges) and discuss the results [0.3 pts]
'''

# Q1. Implementing stack using python arrays

class ArrayStack:
    def __init__(self):
        self._stackArray = []
    def push(self, value):
        self._stackArray.append(value)
    def pop(self):
        if not self._stackArray:    # if item to pop is not in stackArray, return None
            return None
        else:
            return self._stackArray.pop()
    def peek(self):
        if not self._stackArray:    # if item to view is not in stackArray, return None
            return None
        else:
            return self.stackArray[-1]
        
# Q2. Implementing stack with singly-linked list

# Creating a class for the list node
        
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    # getters
    def getValue(self):
        return self._value

    def getNext(self):
        return self._next
        
    # setters
    def setValue(self, value):
        self._value = value
    
    def setNext(self, next):
        self._next = next

    # method for converting to string
    def convertToString(self):
        return str(self._value)

# Creating the singly-linked list based stack

class ListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = Node(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            retrieve_value = self._head.getValue()
            self._head = self._head.getNext()
            return retrieve_value
    def peek(self):
        if self._head is None:
            return None
        else:
            return self._head.getValue()


# Q3. Write a function which generates random lists of 10000 tasks. Each
# task is either a push w/ probability 0.7, or a pop w/ probability 0.3 [0.3 pts]
def generate_tasks(n=10000):
    randomTasks = []
    for _ in range(n):
        task = 'pop' if random.random() < 0.7 else 'push'
        randomTasks.append(task)
    return randomTasks


# Q4. Measure the performance of both implementations on 100 such
# lists of tasks using timeit and print the results [0.3 pts]

# code in progress