import timeit
import matplotlib.pyplot as plt
import numpy as np


# Q1
def linear_search(key, vect):
    for i in range(len(vect)):
        if vect[i] == key:
            return key
    return False

def binary_search(vect, first, last, key):
    if (first <= last):
        mid = (first + last)/2
        if(key == vect[mid]):
            return key
        elif (key < vect[mid]):
            return binary_search(vect, first, mid-1, key)
        elif (key > vect[mid]):
            return binary_search(vect, mid+1, last, key)
    return False    

# Q2
vect1 = []
vect2 = []
vect3 = []
vect4 = []
vect5 = []
vect6 = []

for i in range(1000):
    vect1.append(i)
for i in range(2000):
    vect2.append(i)
for i in range(4000):
    vect3.append(i)
for i in range(8000):
    vect4.append(i)
for i in range(16000):
    vect5.append(i)
for i in range(32000):
    vect6.append(i)

timeL1 = timeit.timeit(lambda: linear_search(999, vect1), number=100)
timeB1 = timeit.timeit(lambda: binary_search(vect1, 1000, 0, 999), number=100)
avgL1 = timeL1/100
avgB1 = timeB1/100

timeL2 = timeit.timeit(lambda: linear_search(999, vect2), number=100)
timeB2 = timeit.timeit(lambda: binary_search(vect2, 2000, 0, 999), number=100)
avgL2 = timeL2/100
avgB2 = timeB2/100

timeL3 = timeit.timeit(lambda: linear_search(999, vect3), number=100)
timeB3 = timeit.timeit(lambda: binary_search(vect3, 4000, 0, 999), number=100)
avgL3 = timeL3/100
avgB3 = timeB3/100

timeL4 = timeit.timeit(lambda: linear_search(999, vect4), number=100)
timeB4 = timeit.timeit(lambda: binary_search(vect4, 8000, 0, 999), number=100)
avgL4 = timeL4/100
avgB4 = timeB4/100

timeL5 = timeit.timeit(lambda: linear_search(999, vect5), number=100)
timeB5 = timeit.timeit(lambda: binary_search(vect5, 16000, 0, 999), number=100)
avgL5 = timeL5/100
avgB5 = timeB5/100

timeL6 = timeit.timeit(lambda: linear_search(999, vect6), number=100)
timeB6 = timeit.timeit(lambda: binary_search(vect6, 32000, 0, 999), number=100)
avgL6 = timeL6/100
avgB6 = timeB6/100

# Q3
element = [1000, 2000, 4000, 8000, 16000, 32000]

avgL = np.array([avgL1, avgL2, avgL3, avgL4, avgL5, avgL6])
avgB = np.array([avgB1, avgB2, avgB3, avgB4, avgB5, avgB6])

plt.scatter(element, avgL)
plt.xlabel("Number of Elements")
plt.ylabel("Average Time")
plt.title("Linear Search")
slope, intercept = np.polyfit(element, avgL, 1)
linevalues = [slope * x + intercept for x in element]
plt.plot(element, linevalues, 'r')
plt.show()

plt.clf()
plt.scatter(element, avgB)
plt.xlabel("Number of Elements")
plt.ylabel("Average Time")
plt.title("Binary Search")





plt.show()


'''
Q5

'''
