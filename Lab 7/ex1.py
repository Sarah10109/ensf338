import random
import timeit
import matplotlib.pyplot as plt
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

def calcbalancetree(root, biggest): 
    if root is not None:
        data = (abs(calcbalance(root))) # Depth-first, pre-order traversal style
        if data > biggest:
            biggest = data
        check2 = calcbalancetree(root.left, biggest)
        check1 = calcbalancetree(root.right, biggest)
        if check1 > biggest:
            biggest = check1
        if check2 > biggest:
            biggest = check2
    return biggest
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right)) #returns the side that keeps going incase one side is None and the other continues

def calcbalance(root):
    if root is None:
        return 0
    return height(root.right) - height(root.left)
xaxis = []
yaxis = []
randoset = [i for i in range(1000)]
for i in range(1000):
    random.shuffle(randoset)
    biggest = 0
    roottest = insert(randoset[0])
    for j in range(1, 1000):
        insert(randoset[j], roottest)
    stime = timeit.timeit(lambda: calcbalancetree(roottest, biggest), number=10)
    value = calcbalancetree(roottest, biggest)
    avgtime = stime / 10
    yaxis.append(avgtime)
    xaxis.append(value)
    
    
plt.scatter(xaxis, yaxis)
plt.show()







