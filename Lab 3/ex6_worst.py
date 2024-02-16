import random
import timeit
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000)

# linear search 
def linear_search(array, num):
    for i in range(len(array)):
        if num == array[i]:
            return i # returns index at which num is located
    return -1 #num not found in array

# Find the index of the greatest element in the array
def find_max_index(arr, low, high):
    max_index = low
    for i in range(low+1, high+1):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def partition(arr, low, high):
    # find index of max element and swap it with last element (this is to make sure
    # the pivot point is the greatest element in the array, which would allow quicksort
    # to undergo the worst case scenario)
    max_index = find_max_index(arr, low, high)
    arr[max_index], arr[high] = arr[high], arr[max_index]

    pivot_point = arr[high]
    i = low - 1
    for index in range(low, high):
        if (arr[index] <= pivot_point):
            i += 1
            (arr[i], arr[index]) = (arr[index], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


# quicksort 
def quicksort_array(arr, low, high):
    if low < high:
        section = partition(arr, low, high)
        # sort left of pivot
        quicksort_array(arr, low, section - 1)
        # sort right of pivot
        quicksort_array(arr, section + 1, high)


def binary_search(array, first, last, num):
    #quicksort_array(array, first, last)
    array.sort()
    while first <= last:
        midpoint = (first + last) // 2
        if num == array[midpoint]:
            return midpoint  # key at which num is located
        elif num < array[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return -1  # num not found in array

# Executing all the components of ex6_avg.py, except with the worst-case scenario for quicksort
# Q2 (6.2.2) and Q3 (6.2.3)
# measure performance on 100 random tasks (i.e search for a constant element in an array that gets reshuffled every time)

# list of the requried array sizes for testing
arrayLengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

# create arrays for average performance times for linear and binary search, respectively
avg_times_linear = []
avg_times_binary = []


for item in arrayLengths:
    # create an array of the specified length
    arrayNum = [a for a in range(item)]
    
    linear_performance_times = [] # empty array to store the 100 different performance times for linear search on array of spefied length
    binary_performance_times = [] # empty array to store the 100 different performance times for binary search on array of specified length

    # assess performance on 100 randomized tasks
    for i in range(100):
        random.shuffle(arrayNum)
        timeLinear = timeit.timeit(lambda: linear_search(arrayNum, 10), number = 1)
        timeBinary = timeit.timeit(lambda: binary_search(arrayNum, 0, len(arrayNum) - 1, 10), number = 1)
        linear_performance_times.append(timeLinear)
        binary_performance_times.append(timeBinary)
      
    # compute average time taken
    linear_avg = sum(linear_performance_times)/len(linear_performance_times)
    binary_avg = sum(binary_performance_times)/len(binary_performance_times)
   
    avg_times_linear.append(linear_avg)
    avg_times_binary.append(binary_avg)


# Q4 (6.2.4) - Plotting
# Plot the above and discuss which algorithm is faster

# plot of array length vs. linear search performance time
plt.plot(arrayLengths, avg_times_linear, label="Linear search", color='green')
plt.plot(arrayLengths, avg_times_binary, label="Binary search", color='blue')
plt.xlabel('Array Length')
plt.ylabel('Performance Time')
plt.title('Array Length vs. Search Performance Time')
plt.legend()
plt.show()

# According to the graph, linear search seems to be faster in this scenario as it has a complexity of O(n) whereas binary
# search has a complexity of O(log n), plus the worst-case complexity for the quicksort algorithm, which is O(n^2).