import random
import timeit
import matplotlib.pyplot as plt

'''
Now, consider the tasks of searching in a sorted array

3. Provide the code for an inefficient implementation and an efficient
implementation. [0.2 pts]

4. State the worst-case complexity of each. [0.2 pts]
'''

# efficient implementation for searching a large sorted array

# interpolation search: returns index of desired element in array; if not found, returns -1
# interpolation search worst case complexity: O(n)

def interpolation_search(arr, x):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1

        pos = lo + ((x - arr[lo]) * (hi - lo)) // (arr[hi] - arr[lo])

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1

        else:
            hi = pos - 1

    return -1


# inefficient implementation for searching a sorted array

# linear search: traverses through every element in array until desired element is found, and returns its index; otherwise, returns -1
# linear search worst case complexity: O(n)
def linear_search(array, num):
    for i in range(len(array)):
        if num == array[i]:
            return i
    return -1


'''
5. Provide the code for an experiment that demonstrates the
difference. [0.2 pts] The experiment should:

    1. Time the execution of both implementations on realistic, large inputs (1000
    elements or above)

    2. Plot the distribution of measured values across multiple measurements (>=
    100 measurements per task) - aka measured times vs. measurement amounts
'''

# Timing the execution of both binary and linear search on arrays of sizes 1000, 2000, 3000

array_sizes = [1000, 2000, 3000]
repeat_times = [100, 200, 300]

results_interpolation = {}
results_linear = {}

for item in array_sizes:
    test_array = [a for a in range(len(array_sizes)+1)]
    
    interpolation_min_times = []
    linear_min_times = []
    for value in repeat_times:
        interpolation_performance_times = []
        linear_performance_times = []

        # for more accurate timing calculations, the average of 100 measurements are used
        interpolation_performance_times = timeit.repeat(lambda: interpolation_search(test_array, 950), number=100, repeat=value)
        interpolation_performance_times = [a/100 for a in interpolation_performance_times]

        linear_performance_times = timeit.repeat(lambda: linear_search(test_array, 950), number=100, repeat=value)
        linear_performance_times = [a/100 for a in linear_performance_times]
        
        # appending the minimum time from list of performance times for said iteration
        interpolation_min_times.append(min(interpolation_performance_times))
        linear_min_times.append(min(linear_performance_times))
    results_interpolation.update({item: interpolation_min_times})
    results_linear.update({item: linear_min_times})


# plotting the data

# Create the plot for binary search
for size, times in results_interpolation.items():
    plt.plot(repeat_times, times, label=f'Interpolation Search Array Size {size}', linestyle='dashed')

# Create the plot for linear search
for size, times in results_linear.items():
    plt.plot(repeat_times, times, label=f'Linear Search Array Size {size}', linestyle='solid')

# Add a legend
plt.legend(loc='upper right')

# Add labels and title
plt.xlabel('Repetition Times')
plt.ylabel('Measured Performance Times')
plt.title('Repetition Values vs. Measured Performance Times for Interpolation and Linear Search on Different Array Sizes', y=1.05)

# Show the plot
plt.show()
