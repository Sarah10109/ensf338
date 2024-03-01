

class myStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]
        
def tostack(arg):
    stack = myStack()
    for i in arg:
        stack.push(i)
    return stack
def calculatebracket(stackarg):
    i = 1
    argcount = 0
    args = ['', '', '']
    while(i):
        stackelement = stackarg.pop()
        if(stackelement == '('):
            stackarg.pop()
            break
        if(stackelement == ')'):
            stackarg.pop()
            args[argcount] = str(calculatebracket(stackarg))
            argcount += 1
        if(stackelement == ' '):
            argcount += 1
            continue
        args[argcount] = stackelement + args[argcount]

    
    # arg[2] should be the sign, while arg[0] should be arg2 and arg[1] should be arg 1
    if(args[2] == '+'):
        return (int(args[1]) + int(args[0]))
    elif (args[2] == '-'):
        return (int(args[1]) - int(args[0]))
    elif (args[2] == '/'):
        return (int(args[1]) / int(args[0]))
    elif (args[2] == '*'):
        return (int(args[1]) * int(args[0]))
    else:
        return 'invalid entry'

stk = tostack('(* (- 2 1) 3)')
stk.pop()
#not working with nested arguments fix later
print(calculatebracket(stk))

        

