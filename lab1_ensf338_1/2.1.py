# Part 2.1 - Find the error

# What the code does:
    # The code takes an integer arguement from the command line and checks whether it is prime or not
    # If number < 2, 'No' will be printed, otherwise a for loop will iterate through a variable i for all numbers from 2 up to (but not including) number
    # If the remainder after dividing number by i is 0, 'No' is printed, indicating a composite number; otherwise, 'Yes' is printed, indicating a prime number 

# Error: There was a small syntax error. Here, at this line, print ('Yes’), the right-side quotation mark was incorrect.  


# Code with fixed errors
import sys

def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print ('Yes')

# Test the function
do_stuff()