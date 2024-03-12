import matplotlib.pyplot as plt
import timeit
import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode
    
def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

random_vector = [random.randint(1, 100000) for _ in range(10000)]
sorted_vector = sorted(random_vector)


rootsort = None
rootrand = None

for i in range(10000):
    insert(sorted_vector[i], rootsort)

random.shuffle(sorted_vector)

for i in range(10000):
    insert(sorted_vector[i], rootrand)

sortedtime = 0
shuffletime = 0
elements = [i for i in range(10000)]
for i in range(10000):
    stime = timeit.timeit(lambda: search(sorted_vector[i], rootsort), number=10)
    rtime = timeit.timeit(lambda: search(sorted_vector[i], rootrand), number=10)
    savg = stime / 10
    ravg = rtime / 10
    sortedtime += (savg)
    shuffletime += (ravg)

print("average of sorted ", sortedtime)
print("Shuffled time: ", shuffletime)

#Shuffled time is most of the time faster. it can be slower but its a low possibility of a bad shuffle that leads to mostly sorted list.




