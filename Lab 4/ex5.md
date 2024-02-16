In class, we have seen two different ways to perform multiple
measures with timeit:
• The first uses the number parameters, as in:
elapsed_time = timeit.timeit(lambda: fibonacci(1000), number=100)
• The second uses the repeat function, as in:
times = timeit.repeat(lambda: fibonacci(1000), repeat =5, number=10)

