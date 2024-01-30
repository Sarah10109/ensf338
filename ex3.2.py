import timeit
import matplotlib.pyplot as plt
import numpy as np

before = """
import json
largeFile = open("large-file.json", encoding="utf8").read()
largeFile = json.loads(largeFile) 

def change(obj, record):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'size':
                obj[key] = 35
            elif isinstance(value, (dict, list)):
                change(value,record)
                
    elif isinstance(obj, list):
            i = 0
            for i, item in enumerate(obj):
                change(item, record)
                if i == record:      
                    break  
"""

testcode1 = """
change(largeFile,1000)
"""
testcode2 = """
change(largeFile,2000)
"""
testcode3 = """
change(largeFile,5000)
"""

testcode4 = """
change(largeFile,10000)
"""

time1 = timeit.timeit(stmt=testcode1,setup=before, number=100)

time2 = timeit.timeit(stmt=testcode2,setup=before, number=100)

time3 = timeit.timeit(stmt=testcode3,setup=before, number=100)

time4 = timeit.timeit(stmt=testcode4,setup=before, number=100)

records = np.array([1000, 2000, 5000, 10000])

avgList = []

average1 = time1/100
avgList.append(average1)

average2 = time2/100
avgList.append(average2)

average3 = time3/100
avgList.append(average3)

average4 = time4/100
avgList.append(average4)

avgArr = np.array(avgList)

slope, intercept = np.polyfit(records, avgArr, 1)
plt.scatter(records, avgArr)
linevalues = [slope * x + intercept for x in records]
plt.plot(records, linevalues, 'r')
plt.xlabel('Number of Records')
plt.ylabel('Average Procseeing Time')
plt.title('Number of Records vs. Average Procseeing Time')
plt.savefig("output.3.2.png")

