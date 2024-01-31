import sys

def do_stuff():
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Incorrect input... goodbye")
        return 

    #missing user input error checking
    if number < 2:
        print("No")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("No")
                return
        print("Yes")
        #either " or ' work but in code had syntax error from using an upper comma ’
    return
#test the function
do_stuff()

#function looks for prime numbers by checking if number divides into every number between 2 and one less than itself.