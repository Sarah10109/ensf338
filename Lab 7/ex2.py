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