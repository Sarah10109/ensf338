import matplotlib.pyplot as plt
import timeit
import numpy as np
import random
import sys 
sys.setrecursionlimit(10000)

# average
def partitionAvg(array, low, high):
    pivot_index = random.randint(low, high)
    array[high], array[pivot_index] = array[pivot_index], array[high]
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
# worst
def partitionW(array, low, high):
    pivot = min(array[low:high+1])
    pivot_index = array.index(pivot)
    array[pivot_index], array[high] = array[high], array[pivot_index]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
# best
def partitionB(array, low, high):
    mid = (high + low) // 2
    pivot = sorted([array[low], array[mid], array[high]])[1]
    pivot_index = array.index(pivot)
    array[pivot_index], array[high] = array[high], array[pivot_index]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high, type):
    if low < high:
        if type == 'worst':
            pi = partitionW(array, low, high)
            quickSort(array, low, pi - 1, type) 
            quickSort(array, pi + 1, high, type)
        elif type == 'avg':
            pi = partitionAvg(array, low, high)
            quickSort(array, low, pi - 1, type) 
            quickSort(array, pi + 1, high, type)
        else:
            pi = partitionB(array, low, high)
            quickSort(array, low, pi - 1, type) 
            quickSort(array, pi + 1, high, type)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


# Q1/2
sizes = [i * 5 for i in range(1, 21)]
time = []

# best case 
for i in range(0, 20):
    globals()[f'array{i+1}'] = list(range(sizes[i]))


# bubble sort
for i in range (1,21):    
    time.append(timeit.timeit(lambda: bubble_sort(globals()[f'array{i}']), number=1000)/1000)

plt.plot(sizes, time, label="Bubble Sort", color='blue')
time.clear()

for i in range (1,21):    
    time.append(timeit.timeit(lambda: quickSort(globals()[f'array{i}'], 0, len(globals()[f'array{i}']) - 1, 'best'), number=1000)/1000)


plt.plot(sizes, time, label="Quick Sort", color='green')
plt.xlabel('Size of Array')
plt.ylabel('Time Taken')
plt.title('Time taken of Each Algorithm in Best Case')
plt.legend()
plt.show()
time.clear()



# worse case
for i in range(0, 20):
    globals()[f'array{i+1}'] = list(range(sizes[i], 0, -1))

# bubble sort
for i in range (1,21):    
    time.append(timeit.timeit(lambda: bubble_sort(globals()[f'array{i}']), number=1000)/1000)


plt.plot(sizes, time, label="Bubble Sort", color='blue')
time.clear()

# quick sort
for i in range (1,21):    
    time.append(timeit.timeit(lambda: quickSort(globals()[f'array{i}'], 0, len(globals()[f'array{i}']) - 1, 'worst'), number=1000)/1000)

plt.plot(sizes, time, label="Quick Sort", color='green')

plt.xlabel('Size of Array')
plt.ylabel('Time Taken')
plt.title('Time taken of Each Algorithm in Worst Case')
plt.legend()
plt.show()
time.clear()





# average case
for i in range(0, 20):
    globals()[f'array{i+1}'] = [random.randint(1, 100) for _ in range(sizes[i])]

for i in range (1,21):    
    time.append(timeit.timeit(lambda: bubble_sort(globals()[f'array{i}']), number=10000)/10000)

plt.plot(sizes, time, label="Bubble Sort", color='blue')
time.clear()


for i in range (1,21):    
    time.append(timeit.timeit(lambda: quickSort(globals()[f'array{i}'], 0, len(globals()[f'array{i}']) - 1, 'avg'), number=10000)/10000)

plt.plot(sizes, time, label="Quick Sort", color='green')

plt.xlabel('Size of Array')
plt.ylabel('Time Taken')
plt.title('Time taken of Each Algorithm in Average Case')
plt.legend()
plt.show()
time.clear()



