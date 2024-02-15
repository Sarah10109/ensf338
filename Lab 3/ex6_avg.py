import random
import timeit
import matplotlib.pyplot as plt

# Q1  (6.2.1)

# linear search 
def linear_search(array, num):
    for i in range(len(array)):
        if num == array[i]:
            return i # returns index at which num is located
    return -1 #num not found in array


# use quicksort to sort the input array, then search it using binary search

# partition
def partition(arr, low, high):

    # select last element of array as pivot
    pivot_point = arr[high]

    i = low - 1

    # iterate through all elments and compare each elemenet with pivot point
    for index in range(low, high):
        if (arr[index] <= pivot_point):
            i += 1
            # swap element at i with element at index
            placeholder = arr[i]
            arr[i] = arr[index]
            arr[index] = placeholder

    
    # Swap pivot with greater element at i
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    # Return partition position
    return i + 1


# quicksort 
def quicksort_array(arr, low, high):
    if low < high:
        section = partition(arr, low, high)

        # sort left of pivot
        quicksort_array(arr, low, section - 1)

        # sort right of pivot
        quicksort_array(arr, section + 1, high)


# binary search
def binary_search(array, first, last, num): 
    if (first <= last):
        midpoint = (first + last)// 2
        if (num == array[midpoint]):
            return midpoint # key at which num is located
        elif (num < array[midpoint]):
            return binary_search(array, first, midpoint-1, num)
        else:
            return binary_search(array, midpoint+1, last, num)
    return -1 # num not found in array


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

        quicksort_array(arrayNum, 0, len(arrayNum) - 1) # sort array before doing binary search
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
plt.plot(arrayLengths, avg_times_linear)
plt.xlabel('Array Length')
plt.ylabel('Performance Time')
plt.title('Array Length vs. Linear Search Performance Time')
plt.show()

# plot of array length vs. binary search performance time
plt.plot(arrayLengths, avg_times_binary)
plt.xlabel('Array Length')
plt.ylabel('Performance Time')
plt.title('Array Length vs. Binary Search Performance Time')
plt.show()

# According to the graphs, binary search is faster as it has a complexity of O(logn) whereas
# linear search depicts a complexity of O(n).