'''
In this exercise, we'll start turning our BST into an AVL tree

Extend the BST implementation from exercise 1 by extending the
insert() method:

1. Implement code to identify the pivot node on node insertion [0.3 pts]

2. Implement code to identify case 1 (pivot does not exist) [0.4 pts]
    • In this case, the code should print “Case #1: Pivot not detected”
    • The code should also update node balances

3. Implement code to identify case 2 (pivot exist but node is being inserted
into shorter subtree) [0.6 pts]
    • In this case, the code should print “Case #2: A pivot exists, and a node was added to
    the shorter subtree”
    • The code should also update node balances

4. Implement four test cases. Each test case consists into adding an
appropriate sequence of nodes: [0.2 pts]
    • Adding a node results in case 1
    • Adding a node results in case 2
    • Adding a node results in case 3 (the code should print “Case 3 not
    supported”)

'''


# Extending the BST from exercise 1 into an AVL tree

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0 # balance attribute

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
    
    # Update the balance of the nodes and determine the pivot node
    pivot = None
    current = newnode
    while current is not None:
        current.balance = calcbalance(current)
        if abs(current.balance) > 1:
            pivot = current
        current = current.parent
   
    # Checking Case #1: Pivot not detected
    if pivot is None:
        print("Case #1: Pivot not detected")
    
    # Checking Case #2: Pivot exists but node is inserted into shorter subtree
    elif (pivot.balance > 0 and newnode.data < pivot.data) or (pivot.balance < 0 and newnode.data > pivot.data):
        print("Case #2: A pivot exists, and a node was added to the shorter subtree")
    else:
        print("Case #3: Not supported") # if none of the above, case 3 must be true, hence the message "Case #3: Not supported" is printed

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

# Checks for Case #3
def check_case_3(root):
    if root is not None:
        if (root.balance > 0 and root.left and root.left.balance > 0) or (root.balance < 0 and root.right and root.right.balance < 0):
            print("Case #3: Not supported")
        check_case_3(root.left)
        check_case_3(root.right)

def leftRotate(node):
    rightChild = node.right
    leftChild = rightChild.left
    rightChild.left = node
    node.right = leftChild
    node.balance = calcbalance(node)
    rightChild.balance = calcbalance(rightChild)
    return rightChild

def rightRotate(node):
    leftChild = node.left
    rightChild = leftChild.right
    leftChild.right = node
    node.left = rightChild
    node.balance = calcbalance(node)
    leftChild.balance = calcbalance(leftChild)
    return leftChild



# Test cases
root = None
root = insert(30, root) # case 1
root = insert(20, root) # case 1
root = insert(40, root) # case 2
root = insert(10, root) # case 3



