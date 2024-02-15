from random import randint
import matplotlib.pyplot as plt
def quicksort(arr, low, high):
    global count
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)




def partition(arr, low, high):
    global count
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        
        while left <= right and arr[left] <= pivot:
            left = left + 1
            count += 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
            count += 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

array1 = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#firstly the pivot will be chosen as 16. 


#Then two sub arrays will be made, one being completly empty and the other containing all other elements
# [15, 14, 13, 12 ,11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [16]
#then the next pivot will be made as the next element
#This will repeat until the last two elements 
#[14, 13, 12 ,11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [15], [16]
#[13, 12 ,11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [14], [15], [16]
#[12 ,11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [13], [14], [15], [16]
#[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [12], [13], [14], [15], [16]
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11], [12], [13], [14], [15], [16]
#[9, 8, 7, 6, 5, 4, 3, 2, 1], [10], [11], [12], [13], [14], [15], [16]
#[8, 7, 6, 5, 4, 3, 2, 1], [9], [10], [11], [12], [13], [14], [15], [16]
#[7, 6, 5, 4, 3, 2, 1], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[6, 5, 4, 3, 2, 1], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[5, 4, 3, 2, 1], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[4, 3, 2, 1], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[3, 2, 1], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[2, 1], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[1, 2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16]

count = 0
quicksort(array1, 0, 15)


n = []
values = [10, 20, 30, 40]

arr1 = [-i for i in range(10)]
arr2 = [-i for i in range(20)]
arr3 = [-i for i in range(30)]
arr4 = [-i for i in range(40)]

count = 0
quicksort(arr1, 0, 9)
n.append(count)

count = 0
quicksort(arr2, 0, 19)
n.append(count)

count = 0
quicksort(arr3, 0, 29)
n.append(count)

count = 0
quicksort(arr4, 0, 39)
n.append(count)

plt.plot(values, n, label='Comparisons')


plt.xlabel('Array Size')
plt.ylabel('Comparrisons')
plt.title('QuickSort Performance')

plt.legend()

plt.show()