import timeit
import matplotlib.pyplot as plt
import numpy as np

before = """
import json
largeFile = open("large-file.json", encoding="utf8").read()
largeFile = json.loads(largeFile) 

def change(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'size':
                obj[key] = 35
            elif isinstance(value, (dict, list)):
                change(value)
                
    elif isinstance(obj, list):
            i = 0
            for i, item in enumerate(obj):
                change(item)
                if i == 1000:      
                    break  
"""

testcode = """
change(largeFile)
"""


time = timeit.repeat(stmt=testcode,setup=before, repeat=1000, number=1)

arrTime = np.array(time)

plt.hist(arrTime, color='skyblue', edgecolor='black')
plt.xlabel('Measured Times')
plt.ylabel('Frequency')
plt.title('Distribution of the Measured Times')
plt.savefig("output.3.3.png")