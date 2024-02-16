# First, Consider the following code:
def processdata(li):           
    for i in range(len(li)):    # 2 ops x n
        if li[i] > 5:           # 2 ops x (n-1)
            for j in range(len(li)):    # 2 ops x (n-1)
                li[i] *= 2              # 2 ops x (n-1)


# 1. State and justify what is the best, worst and average case
# complexity for the code in the previous slide [0.2 pts]
'''
See the annotations made to the code snippet above. 
Best case: 2n + 2(n-1) = 4n-1 --> O(n)
Worst case: 2n + 6(n-1) = 8n-1 --> O(n)
'''
                
# 2. Are average, best, and worst case complexity the same? If not,
# produce a modified version of the code above for which average,
# best, and worst case complexity are equivalent. [0.2 pts]

# Answer: Yes. Average, best, and worst case complexity is the same.
