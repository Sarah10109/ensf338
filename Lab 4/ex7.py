import timeit
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def get_element_at_pos(self, position):
        if position < 0:
            return None
        current = self.head
        for _ in range(position):
            if current is None:
                return None
            current = current.next
        return current

    def reverseold(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead
    
    def reversenew(self):
        current = self.head
        previous = None
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous


## Populate the lists

def createlist(size):
    linkedlist = LinkedList()
    for i in range(1, size):
        linkedlist.insert_at_head(i)
    return linkedlist

linklist1000 = createlist(1001)
linklist2000 = createlist(2001)
linklist3000 = createlist(3001)
linklist4000 = createlist(4001)

x_axis = [1000, 2000, 3000, 4000]

timeRO1 = timeit.timeit(lambda: linklist1000.reverseold(), number=100)
timeRO2 = timeit.timeit(lambda: linklist2000.reverseold(), number=100)
timeRO3 = timeit.timeit(lambda: linklist3000.reverseold(), number=100)
timeRO4 = timeit.timeit(lambda: linklist4000.reverseold(), number=100)

avgRO1 = timeRO1/100
avgRO2 = timeRO2/100
avgRO3 = timeRO3/100
avgRO4 = timeRO4/100


timeRN1 = timeit.timeit(lambda: linklist1000.reversenew(), number=100)
timeRN2 = timeit.timeit(lambda: linklist2000.reversenew(), number=100)
timeRN3 = timeit.timeit(lambda: linklist3000.reversenew(), number=100)
timeRN4 = timeit.timeit(lambda: linklist4000.reversenew(), number=100)

avgRN1 = timeRN1/100
avgRN2 = timeRN2/100
avgRN3 = timeRN3/100
avgRN4 = timeRN4/100

avgold = np.array([avgRO1, avgRO2, avgRO3, avgRO4])
avgnew = np.array([avgRN1, avgRN2, avgRN3, avgRN4])


plt.plot(x_axis, avgold, color='red')
plt.xlabel("Number of Elements")
plt.ylabel("Average Time of old")
plt.show()

plt.plot(x_axis, avgnew, color='g')
plt.xlabel("Number of Elements")
plt.ylabel("Average Time of new")
plt.show()


