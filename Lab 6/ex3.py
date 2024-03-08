# equation = input('Proivde number: ')
# answer = 
# print(answer)


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data):
        if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
        else:
            self.data = data
    
    def postorder(root):
        if root is not None:
            postorder(root.left)
            postorder(root.right)
            print(root.data)
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.data),
      if self.right:
         self.right.PrintTree()
    



example = '( 1 + 2 )'
exampleList = example.split()
count = 0;
# for i in range(len(exampleList)):
#     if exampleList[i] == '(':
#         count += 1
#     else:

#     print(exampleList[i])


tree = Node(exampleList[2])
tree.insert(exampleList[1])
tree.insert(exampleList[3])
tree.PrintTree()