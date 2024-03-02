import sys

class myStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
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
            break
        if(stackelement == ')'):
            args[argcount] = str(calculatebracket(stackarg))
            argcount += 1
            if(stackarg.peek() == ' '):
                stackarg.pop()
            continue
        if(stackelement == ' '):
            argcount += 1
            continue
        args[argcount] = stackelement + args[argcount]

    
    # arg[2] should be the sign, while arg[0] should be arg2 and arg[1] should be arg 1
    if(args[2] == '+'):
        return (float(args[1]) + float(args[0]))
    elif (args[2] == '-'):
        return (float(args[1]) - float(args[0]))
    elif (args[2] == '/'):
        return (float(args[1]) / float(args[0]))
    elif (args[2] == '*'):
        return (float(args[1]) * float(args[0]))
    else:
        return 'invalid entry'


userarg = str(sys.argv[1])
stk = tostack(userarg)
stk.pop()
print(calculatebracket(stk))

        

