# Turn the AVL tree of Exercise 3 into a fully grown AVL tree

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
            print("Case #3a: Adding a node to an outside subtree")
            new_root = _left_rotate(pivot)
            if pivot == root:
                root = new_root
        elif (pivot.balance < 0 and pivot.left and newnode.data < pivot.left.data):
            print("Case #3a: Adding a node to an outside subtree")
            new_root = _right_rotate(pivot)
            if pivot == root:
                root = new_root
        else: # Q3
            # Checking Case #3b: adding a node to an inside subtree
            if (pivot.balance > 0 and pivot.right and newnode.data < pivot.right.data):
                print("Case #3b: Adding a node to an inside subtree")
                root = _rl_rotate(pivot)
            elif (pivot.balance < 0 and pivot.left and newnode.data > pivot.left.data):
                print("Case #3b: Adding a node to an inside subtree")
                root = _lr_rotate(pivot)
    
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

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right)) #returns the side that keeps going incase one side is None and the other continues

def calcbalance(root):
    if root is None:
        return 0
    return height(root.right) - height(root.left)

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
    return right_child  

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
    return left_child

# Q1
def _lr_rotate(node):
    node.left = _left_rotate(node.left)
    return _right_rotate(node)

# Q2
def _rl_rotate(node):
    node.right = _right_rotate(node.right)
    return _left_rotate(node)

# Test cases
root = None
root = insert(30, root) # case 1
root = insert(20, root) # case 1
root = insert(40, root) # case 2
root = insert(10, root) # case 3a
# Q4
root = insert(25, root) # case 3b (RL)
root = insert(35, root) # case 3b (LR)