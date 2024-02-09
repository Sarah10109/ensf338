import matplotlib.pyplot as plt
from random import randint



def bubble_sort(arr):
    global noc
    global nos
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            noc += 1
            if arr[j] > arr[j+1]:
                nos += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
nums = [1000, 2000, 4000, 8000, 16000, 32000]
comp = []
swap = []

arr1000 = [randint(1, 1000) for i in range(1000)]

arr2000 = [randint(1, 2000) for i in range(2000)]

arr4000 = [randint(1, 4000) for i in range(4000)]

arr8000 = [randint(1, 8000) for i in range(8000)]

arr16000 = [randint(1, 16000) for i in range(16000)]

arr32000 = [randint(1, 32000) for i in range(32000)]

noc = 0
nos = 0

bubble_sort(arr1000)

comp.append(noc)
swap.append(nos)

noc = 0
nos = 0

bubble_sort(arr2000)

comp.append(noc)
swap.append(nos)

noc = 0
nos = 0

bubble_sort(arr4000)

comp.append(noc)
swap.append(nos)

noc = 0
nos = 0

bubble_sort(arr8000)

comp.append(noc)
swap.append(nos)

noc = 0
nos = 0

bubble_sort(arr16000)

comp.append(noc)
swap.append(nos)

noc = 0
nos = 0

bubble_sort(arr32000)

comp.append(noc)
swap.append(nos)


plt.plot(nums, comp, label='Comparisons')
plt.plot(nums, swap, label='Swaps')

plt.xlabel('Array Size')
plt.ylabel('Count')
plt.title('Bubble Sort Performance')

plt.legend()

plt.show()

