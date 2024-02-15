# 1. Implement a standard binary search, with the following tweak: the
# midpoint for the first iteration must be configurable (all successive
# iterations will just split the array in the middle)

def binary_search(array, first, last, num, initial_midpoint=None):
    while first <= last:
        if initial_midpoint is not None:
            midpoint = initial_midpoint
            initial_midpoint = None  # reset to None to ensure the initial midpoint is used only for the first iteration
        else:
            midpoint = (first + last) // 2
        if num == array[midpoint]:
            return midpoint  # key at which num is located
        elif num < array[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return -1  # num not found in array


# 2. Time the performance of each search task w/ different midpoints
# for each task. You can use whatever strategy you want to check
# different midpoints. Then, choose the best midpoint for each task 



# 3. Produce a scatterplot visualizing each task and the corresponding
# chosen midpoint

# 4. Comment on the graph. Does the choice of initial midpoint appear
# to affect performance? Why do you think is that?