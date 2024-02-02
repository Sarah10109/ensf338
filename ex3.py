import timeit
import cProfile
p = cProfile.Profile()

def sub_fraction(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_fraction(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_fraction(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


p.enable()

test_function()
third_function()

p.disable()

p.print_stats()


'''
QUESTION 1:
A profiler creates a set of statistics that describe how often and for
how long sections of a code are executed.
This data can be accessed in formatted reports using the pstats module.

QUESTION 2
Profiling allows for you to determine how well certain parts of your code perform
while benchmarking is more for testing specific datasets and how the code
overall performs

QUESTION 4
From the data table, I can see thatthe call to third_function is taking the majority of the time to run.
As shown in the output, it is called once but took a total time of 22.922 seconds. 
Meanwhile the rest of the functions were faster than 0.001 im guessing as the total time for the rest of the functions are registered as 0.
'''