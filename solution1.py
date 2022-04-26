# Write code for algorithm 1 below
# Write a program that takes a 
# positive number as an argument and prints the numbers from n to zero.


def program(num):
    #Base Case
    if num == 0:
        return
    #Recursive Case
    else:
        print(num)
        program(num-1)
