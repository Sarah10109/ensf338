# Extending the BST from exercise 2 into an AVL tree

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
    else: #Q3
        # Checking Case #3a: adding a node to an outside subtree
        if (pivot.balance > 0 and pivot.right and newnode.data > pivot.right.data):
            print("Case #3a: adding a node to an outside subtree")
            root = _left_rotate(pivot)
        elif (pivot.balance < 0 and pivot.left and newnode.data < pivot.left.data):
            print("Case #3a: adding a node to an outside subtree")
            root = _right_rotate(pivot)
        else:
            # Checking Case #3b: adding a node to an inside subtree
            print("Case 3b not supported") 
    
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

# Q1
def _left_rotate(node):
    right_child = node.right
    node.right = right_child.left
    if right_child.left is not None:
        right_child.left.parent = node
    right_child.parent = node.parent
    if node.parent is None:
        root = right_child
    elif node == node.parent.left:
        node.parent.left = right_child
    else:
        node.parent.right = right_child
    right_child.left = node
    node.parent = right_child
    node.balance = calcbalance(node)
    right_child.balance = calcbalance(right_child)
    return root

# Q2
def _right_rotate(node):
    left_child = node.left
    node.left = left_child.right
    if left_child.right is not None:
        left_child.right.parent = node
    left_child.parent = node.parent
    if node.parent is None:
        root = left_child
    elif node == node.parent.right:
        node.parent.right = left_child
    else:
        node.parent.left = left_child
    left_child.right = node
    node.parent = left_child
    node.balance = calcbalance(node)
    left_child.balance = calcbalance(left_child)
    return root


# Test cases
root = None
root = insert(30, root) # case 1
root = insert(20, root) # case 1
root = insert(40, root) # case 2
# Q4
root = insert(10, root) # case 3
root = insert(25, root) # case 3b