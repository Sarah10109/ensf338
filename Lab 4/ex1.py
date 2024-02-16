import matplotlib.pyplot as plt
import timeit
import numpy as np

class LinkedList:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def insert(self, new_data):
            new_node = LinkedList(new_data)
            if self.data:
                current = self
                while(current.next):
                    current = current.next
                current.next = new_node
            else:
                self.data = new_data

def middle(start, last):
    # if list is empty
    if start is None:
        return None

    slow = start
    fast = start

    while fast.next != last and fast.next.next != last:
        fast = fast.next.next
        slow = slow.next

    return slow

# Implementing the Binary Search
def binary_search(list_head, target):
    start = list_head
    last = None

    while last != start:
        # Find middle
        mid = middle(start, last)

        # If middle is empty
        if mid is None:
            return None

        # If target is present at middle
        if mid.data == target:
            return mid

        # If target is more than mid
        elif mid.data < target:
            start = mid.next

        # If the target is less than mid.
        else:
            last = mid

    # target not present
    return None


class Array:
    def __init__(self):
        self.array = []

    def insert(self, num):
        self.array.append(num)
        self.array.sort()

    def binary_searchArr(self, num):
        low = 0
        high = len(self.array) - 1

        while low <= high:

            mid = low + (high - low)//2

            if self.array[mid] == num:
                return mid

            elif self.array[mid] < num:
                low = mid + 1

            else:
                high = mid - 1

        return -1

'''
Question 4
The time complexity of for a linked lists is O(n) that is because the algorithm still goes through 
every node in the linked list. It isn't possible to skip over elements since to go through each node 
to find the desired element. So the n would be each node the algorithm needs to go through. 
'''
if __name__ == "__main__":
    sizes = [1000, 2000, 4000, 8000]
    results_array = []
    results_linked_list = []
    for size in sizes:
            arr = Array()
            ll = LinkedList()
            for i in range(size):
                arr.insert(i)
                ll.insert(i)

            search_num = np.random.randint(0, size)

            result_array = timeit.timeit(lambda: arr.binary_searchArr(search_num), number=10000)/10000
            results_array.append(result_array)

            result_linked_list = timeit.timeit(lambda: binary_search(ll, search_num), number=10000)/10000
            results_linked_list.append(result_linked_list)
    
    coefficients_array = np.polyfit(sizes, results_array, 2)
    coefficients_linked_list = np.polyfit(sizes, results_linked_list, 2)

    # Create a function based on the fit
    poly_array = np.poly1d(coefficients_array)
    poly_linked_list = np.poly1d(coefficients_linked_list)

    # Generate y-values for the interpolation function
    y_values_array = poly_array(sizes)
    y_values_linked_list = poly_linked_list(sizes)
    plt.plot(sizes, y_values_array, label='Interpolation Array')
    plt.plot(sizes, y_values_linked_list, label='Interpolation Linked List')

    plt.scatter(sizes, results_array)
    plt.scatter(sizes, results_linked_list)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()


