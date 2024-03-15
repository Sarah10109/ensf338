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

def calcbalancetree(root, balarray): 
    if root is not None:
        balarray.append(calcbalance(root)) # Depth-first, pre-order traversal style
        calcbalancetree(root.left, balarray)
        calcbalancetree(root.right, balarray)
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right)) #returns the side that keeps going incase one side is None and the other continues

def calcbalance(root):
    if root is None:
        return 0
    return height(root.right) - height(root.left)
