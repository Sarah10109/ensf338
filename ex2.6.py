import timeit

def fact(n):
    total = n
    while(n):
        if((n-1) == 0):
            break
        total = total * (n-1)
        n = n - 1
    return total

time = timeit.timeit(lambda: fact(100), number=10000)


def forfact(n):
    if(n > 100):
        print("you done fucked up")
        exit()
    
    total = []
    for i in range(n, 101):
        total.append(fact(i))
    return total
        
def listfact(n):
    if(n > 100):
        print("you done fucked up")
        exit()
    listn = [fact(i) for i in range(n, 100)]

    return listn

timefor = timeit.timeit(lambda: forfact(50), number=1000)

timelist = timeit.timeit(lambda: listfact(50), number=1000)
print(timefor)
print(timelist)