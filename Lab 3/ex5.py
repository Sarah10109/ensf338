import matplotlib.pyplot as plt
import timeit
import numpy as np
import random
import sys 
sys.setrecursionlimit(10000)
# Q1
def binary_search(array, num, start, end):
    if start == end:
        if array[start] > num:
            return start
        else:
            return start+1
    if start > end:
        return start
 
    mid = (start+end)//2
    if array[mid] < num:
        return binary_search(array, num, mid+1, end)
    elif array[mid] > num:
        return binary_search(array, num, start, mid-1)
    else:
        return mid
 
 
def insertion_sortB(array):
    for i in range(1, len(array)):
        num = array[i]
        j = binary_search(array, num, 0, i-1)
        array = array[:j] + [num] + array[j:i] + array[i+1:]


def insertion_sort(array):
    for i in range(1, len(array)):
        num = array[i]
        j = i - 1
        while j >= 0 and num < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = num
    

# Q2,3
sizes = [i * 25 for i in range(1, 11)]
time = []

for i in range(0, 10):
    globals()[f'array{i+1}'] = [random.randint(1, 100) for _ in range(sizes[i])]

# Binary
for i in range (1,11):    
    time.append(timeit.timeit(lambda: insertion_sortB(globals()[f'array{i}']), number=1000)/1000)

plt.plot(sizes, time, label="Binary", color='blue')
time.clear()   

# Traditional

for i in range (1,11):    
    time.append(timeit.timeit(lambda: insertion_sort(globals()[f'array{i}']), number=1000)/1000)

plt.plot(sizes, time, label="Traditional", color='green')


plt.xlabel('Size of Array')
plt.ylabel('Time Taken')
plt.title('Time taken of Each Algorithm in Average Case')
plt.legend()
plt.show()





