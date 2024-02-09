# Q1

# linear search algorithm - return the index at which num in array is located
# if num not in array, return -1
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