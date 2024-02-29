'''
Question 1
The list makes more room when it's full. This is called over-allocation. This is done in 
the line of code (line 70): new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;. 
This line calculates the new size of the array by adding an eighth of the current size (newsize >> 3) 
and a small constant (6) to the current size (newsize). The result is then rounded down to 
the nearest multiple of 4 by bitwise and with the complement of 3 (& ~(size_t)3). This ensures 
that the allocated size is always a multiple of 4, which can be beneficial for memory alignment. 
If the new size is closer to the overallocated size than to the old size, the function rounds 
the new size up to the nearest multiple of 4. This is done in the lines of code (line 74-75): 
if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize)) and 
new_allocated = ((size_t)newsize + 3) & ~(size_t)3;. This is done to avoid overallocation 
when the new size is significantly larger than the old size.
'''

# Q2
import sys
# Create an empty list
lst = []

# Store the initial size of the list
last_size = sys.getsizeof(lst)

# Loop from 0 to 63
for i in range(64):
    # Add an integer to the list
    lst.append(i)

    # Get the current size of the list
    current_size = sys.getsizeof(lst)

    # If the size has changed, print a message
    if current_size != last_size:
        print(f"Capacity changed after adding element {i}, new capacity is {current_size} bytes")
        # Update the last size
        last_size = current_size

# Q3
import timeit
import numpy as np
import matplotlib.pyplot as plt
def grow_array():
    S = 52
    arr = [0] * S
    arr.append(1)
# Measure the time for 1000 iterations
time_taken = []
for i in range(1000):
    time_taken.append(timeit.timeit(grow_array, number=1000)/1000)
time1 = np.array(time_taken)
plt.hist(time1, color='skyblue', edgecolor='black', label='Size S to S+1')

# Q4
def grow2_array():
    S = 51
    arr = [0] * S
    arr.append(1)

time_taken2 = []
for i in range(1000):
    time_taken2.append(timeit.timeit(grow2_array, number=1000)/1000)
time2 = np.array(time_taken2)
plt.hist(time2, color='green', edgecolor='black', alpha=0.5, label='Size S-1 to S')
plt.xlabel('Time Taken')
plt.ylabel('Frequency')
plt.title('Measurements of Growing the Array')
plt.legend()

plt.show()

'''
Question 5
The average time it takes to grow the array from size S-1 to S takes less time than the 
average time it takes to grow the array from size S to S+1. That is because when the largest 
size S will expand when an element is added in this case S+1, because the process involves 
allocating a new, larger memory block, copying the existing elements from the old array to the 
new one, and updating the array's capacity accordingly. While S-1 to S doesn't need to expand 
the capacity of the array so less time is need to allocate a new, larger memory block, copying 
the existing elements from the old array to the new one
'''