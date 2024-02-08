'''
Q1
The code gets an integer n and check if n is equal to 1 or 0. 
If not then it the functions calls it self as a recursion function. 
This code is finding the fibonacci sequence to the nths place.  
'''

'''
Q2
This example is a bad example of divide-and-conquer algorithm since 
it is creating a new problem without making the problem smaller.
The function does split up the work function into smaller parts which 
will go to smaller parts untill n reaches 1 or 0.
'''

'''
Q3
The time complexity of the algorithm is O(2^n)
'''
# Q4
def func2(n):
    fibSeq = [0, 1]
    for i in range(2, n+1):
        fibSeq.append(fibSeq[i-1] + fibSeq[i-2])
    return fibSeq[n]

'''
Q5
The time complexity would be O(n) since the default values are set so 
the only concern is n which is greater than 1. However the functions only 
runs until that value of n is called that amount of time. So the work 
done is only n amount so it would be O(n).
'''

# Q6
import timeit
import numpy as np
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

nums = []
ogCode = []
impCode = []
for i in range (0, 36):
    nums.append(i)
    ogCode.append(timeit.timeit(lambda: func(i), number=1))
    impCode.append(timeit.timeit(lambda: func2(i), number=1))

numAr = np.array(nums)
ogCodeAr = np.array(ogCode)
impCodeAr = np.array(impCode)
plt.scatter(numAr,ogCodeAr )
plt.xlabel('Integer')
plt.ylabel('Procseeing Time')
plt.title('Integers vs. Procseeing Time for Original Code')
plt.savefig("ex1.6.1.jpg")
plt.clf()
plt.scatter(numAr,impCodeAr)
plt.xlabel('Integer')
plt.ylabel('Procseeing Time')
plt.title('Integers vs. Procseeing Time for Improved Version')
plt.savefig("ex1.6.2.jpg")

