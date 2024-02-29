# First, Consider the following code:
def processdata(li):           
    for i in range(len(li)):    # executes n times
        if li[i] > 5:           # condition checked n times for each iteration of for loop
            for j in range(len(li)):    # executes n times
                li[i] *= 2              


# 1. State and justify what is the best, worst and average case
# complexity for the code in the previous slide [0.2 pts]
'''
See the annotations made to the code snippet above. 

Best case: O(n) --> In the best case, there are no elements in li that are >5, so the
for loop inside the if statement won't run at all. This leaves only the outer for loop 
iterating through the array n times, resulting in an O(n) complexity.

Worst case: O(n^2) --> In the worst case, all elements in the array satisfy the condition
that they're >5, so the nested for loop is executed in each iteration of the outer for loop,
resulting in the worst case complexity O(n^2).

Average case: O(n^2) --> The average case is the same as the worst case, as some elements may
satisfy the if condition and some may not, so the nested for loop may still execute for some iterations
of the outer for loop.
'''
                
# 2. Are average, best, and worst case complexity the same? If not,
# produce a modified version of the code above for which average,
# best, and worst case complexity are equivalent. [0.2 pts]

'''
The best case has linear complexity while the average and worst cases have quadratic complexity,
hence the three cases do not have the same complexity. A modification of the code is provided below,
where the nested for loop inside the if statement was removed and an equivalent iterative approach
with enumerate was used to make the best, worst, and average cases have the same complexity, O(n).
'''

def processdata1(li):
    for i, x in enumerate(li):
        if x > 5:
            li[i] = x * 2
# In this code, regardless of whether the code inside the if statement was executed or not, the for loop
# will go through the array once, leading to a best, worst, and average case complexity of O(n).