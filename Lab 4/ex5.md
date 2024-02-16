### In class, we have seen two different ways to perform multiple measures with timeit: 
## • The first uses the number parameters, as in: elapsed_time = timeit.timeit(lambda: fibonacci(1000), number=100)
## • The second uses the repeat function, as in: times = timeit.repeat(lambda: fibonacci(1000), repeat =5, number=10)

### These approaches are designed to deal with different types of measurement noise. Think about what happens when we try to time a program, and which types of issues may result in an incorrect measurement. Reflect on how the two approaches (timeit and repeat) attempt to address these issues. Discuss when it is appropriate to use one or the other. [0.5 pts]

Depending on the situation, running multiple trials of timing may give different results. This is due to many factors, some of them being: the compile time included in the timing measurement, delays/errors in compiling, and overall lagging, which can affect the performance time value from trial to trial for the same code snippet. The timeit method measures the execution time of a code snippet, and aims to reduce these descrepancies by running the code snippet according to a specified number. This reduces discrepancies by conducting multiple trials. Furthermore, if timeit has a specified repeat field, timeit() is called the number of times specified by repeat.

For measuring small code snippets timeit without specifying a repeat value is sufficient, while a repeat value may be more appropriate for timing longer or more complex code.

### Typically, the output of timeit is post-processed to compute some sort of aggregate statistics. Let’s only consider three: average, min,and max. Which one is the appropriate statistic to apply to the output of timeit.timeit()? What is the appropriate statistics to apply to the output of timeit.repeat()? Discuss why. [0.5 pts]

Average is an appropriate statistic to apply to the output of timeit.timeit() since taking the average of the number of times the code snippet was run provides a more accurate value for the performance time. On the other hand, calculating the max and min for the output of iteit.repeat() would help to identify the greatest or lowest time value from all the times that timeit was repeatedly called.

