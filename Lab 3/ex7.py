import timeit
import json
import matplotlib.pyplot as plt

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

# arrMain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# midpoints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arrTasks = [0, 4, 3, 5]


with open('ex7data.json', 'r') as arrayFile:
    data = json.load(arrayFile)

arrMain = data

with open('ex7tasks.json', 'r') as taskFile:
    data1 = json.load(taskFile)

arrTasks = data1

midpoints = data1

def time_search_tasks(arrMain, arrTasks, midpoints):
    # an array to store the best midpoint for each task
    best_midpoints = []

    # Iterate over each task
    for task in arrTasks:
        best_time = None
        best_midpoint = None

        # Try each midpoint
        for midpoint in midpoints:
            elapsed_time = timeit.timeit(lambda: binary_search(arrMain, 0, len(arrMain) - 1, task, initial_midpoint=midpoint), number=1)

            # update the best midpoint and best time
            if best_time is None or elapsed_time < best_time:
                best_time = elapsed_time
                best_midpoint = midpoint

        # Store the best midpoint for this task
        best_midpoints.append(best_midpoint)

    return best_midpoints

optimal_midpoints = time_search_tasks(arrMain, arrTasks, midpoints)
print(optimal_midpoints)



# 3. Produce a scatterplot visualizing each task and the corresponding
# chosen midpoint

# Scatterplot
plt.scatter(arrTasks, optimal_midpoints)
plt.xlabel('Tasks')
plt.ylabel('Midpoints')
plt.title('Scatterplot of Tasks and Corresponding Midpoints')
plt.show()


# 4. Comment on the graph. Does the choice of initial midpoint appear
# to affect performance? Why do you think is that?