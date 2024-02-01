import json
import matplotlib.pyplot as plt
import numpy as np

spotify = open('songdata.json').read()
spotify = json.loads(spotify)

below = []
above = []
for i in range(len(spotify)):
    if(spotify[i]["loudness"] < -8):
        below.append(spotify[i]) 
    elif(spotify[i]["loudness"] > -8):
        above.append(spotify[i])
# below
dataB = []
for i in range(len(below)):
    dataB.append(below[i]["tempo"])
arrB = np.array(dataB)

# above
dataA = []
for i in range(len(above)):
    dataA.append(above[i]["tempo"])
arrA = np.array(dataA)

plt.hist(arrA, color='skyblue', edgecolor='black')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.title('Tempo of Songs Above Loudness -8')
plt.savefig("hist1.png") 
plt.clf()
plt.hist(arrB, color='skyblue', edgecolor='black')
plt.xlabel('Tempo')
plt.ylabel('Frequency')
plt.title('Tempo of Songs Below Loudness -8') 
plt.savefig("hist2.png")



