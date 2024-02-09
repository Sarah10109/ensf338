import random
import timeit

# Q1  (6.2.1)

# linear search algorithm: returns the index at which num in array is located. If num not in array, returns -1
def linear_search(array, num):
    for i in range(len(array)):
        if num == array[i]:
            return i
    return -1


# use quicksort to sort the input array, then search it using binary search
    # quicksort: work-in-progress

# search array using binary search
def binary_search(array, first, last, num):
    if (first <= last):
        midpoint = (first + last)/ 2
        if (num == midpoint):
            return midpoint #key at which num is located
        else if (num < array[midpoint]):
            return binary_search(array, first, midpoint-1, num)
        else:
            return binary_search(array, midpoint+1, last, num)
    return -1 # num not found in array


# Q2 (6.2.2) and Q3 (6.2.3)

# measure performance on 100 random tasks (i.e search for a constant element in an array
# that gets reshuffled every time)


# list of the requried array sizes for testing
arrayLengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

#  create arrays for average performance times for linear and binary search, respectively
avg_times_linear = []
avg_times_binary = []

for item in arrayLengths:
    # create an array of the specified length
    arrayNum = [a for a in range(arrayLengths)]
    linear_performance_times = [] # empty array to store the 100 different performance times for linear search on array of spefied length
    binary_performance_times = [] # empty array to store the 100 different performance times for binary search on array of specified length
   
    # assess performance on 100 randomized tasks
    for i in range(100):
        random.shuffle(arrayNum)
        timeLinear = timeit.timeit("linear_search(10, arrayNum)", number = 1)
        timeBinary = timeit.timeit("binary_search(10, arrayNum)", number = 1)
       
        linear_performance_times.append(timeLinear)
        binary_performance_times.append(timeBinary)
    
    #compute average time taken
    linear_avg = sum(linear_performance_times)/len(linear_performance_times)
    binary_avg = sum(binary_performance_times)/len(binary_performance_times)
   
    avg_times_linear.append(linear_avg)
    avg_times_binary.append(binary_avg)

    # print statement to check output
    print("Average time for linear search on list of length %d: %f" % (item, linear_avg))
    print("Average time for binary search on list of length %d: %f" % (item, binary_avg))



# plot the average time vs list length