import random
import timeit
import matplotlib.pyplot as plt

'''
Now, consider the tasks of searching in a sorted array

3. Provide the code for an inefficient implementation and an efficient
implementation. [0.2 pts]

4. State the worst-case complexity of each. [0.2 pts]

5. Provide the code for an experiment that demonstrates the
difference. [0.2 pts] The experiment should:

    1. Time the execution of both implementations on realistic, large inputs (1000
    elements or above)

    2. Plot the distribution of measured values across multiple measurements (>=
    100 measurements per task)

'''

# efficient implementation for searching a sorted array

# binary search: returns index of desired element in array; if not found, returns -1
# binary search worst case complexity: O(log n)
def binary_search(array, first, last, num): 
    if (first <= last):
        midpoint = (first + last)// 2
        if (num == array[midpoint]):
            return midpoint
        elif (num < array[midpoint]):
            return binary_search(array, first, midpoint-1, num)
        else:
            return binary_search(array, midpoint+1, last, num)
    return -1

# inefficient implementation for searching a sorted array

# linear search: traverses through every element in array until desired element is found, and returns its index; otherwise, returns -1
# linear search worst case complexity: O(n)
def linear_search(array, num):
    for i in range(len(array)):
        if num == array[i]:
            return i
    return -1


# experiment
# code in progress