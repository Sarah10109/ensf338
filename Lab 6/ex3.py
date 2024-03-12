import sys

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def prec(c):
    if c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def infix_to_postfix(s):
    result = []
    stack = []
    i = 0
    while i < len(s):
        c = s[i]

        if c.isdigit():  # Handle multi-digit numbers
            num = c
            while i + 1 < len(s) and (s[i + 1].isdigit() or s[i + 1] == '.'):
                i += 1
                num += s[i]
            result.append(num)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('
        else:
            while stack and prec(c) <= prec(stack[-1]):
                result.append(stack.pop())
            stack.append(c)
        i += 1

    while stack:
        result.append(stack.pop())

    return result

def expressTree(expression):
    stack = []
    for token in expression:
        if is_number(token):  # If operand, push onto stack as a TreeNode
            stack.append(TreeNode(token))
        else:  # If operator, pop two operands, make them children, and push back onto stack
            node = TreeNode(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

def postOrder(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        # Convert to float or int depending on the content
        return float(root.data) if '.' in root.data else int(root.data)

    left_value = postOrder(root.left)
    right_value = postOrder(root.right)

    if root.data == "+":
        return left_value + right_value
    elif root.data == "-":
        return left_value - right_value
    elif root.data == "/":
        result = left_value / right_value
        # Return result as int if it's a whole number, else as float
        return result if result % 1 else int(result)
    else:  # Assuming multiplication for any other case
        return left_value * right_value   

expression = str(sys.argv[1])
expression = ''.join(expression.split(" "))
postfix_expression = infix_to_postfix(expression)
root = expressTree(postfix_expression)
print(postOrder(root))