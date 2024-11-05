"""
Tanvir Rahim
ICS3U
Programming Assignment #2 - Due 11/08/2024
"""

def factors(N):
# Defines a function that determines factors of a number that are less than its square root
    facs = [1]   
    # Declares the variable 'facs' which will represent the list of factors for the number (N)
    for i in range(2, m.floor(m.sqrt(N))+1):
        # Iterates a range from 2 (1 is already in the 'facs' array) to the square root of 'N'
        if N % i == 0:
        # If i, in the range above, is divisible by N with no remainder, it is a factor of N
            facs.append(i)
            # The i value will be added onto the array 'facs' if it is a factor of N
    return facs
    # Returns the array of factors of N that are less than the square root of N

import math as m
# Imports python's math library, and sets it as 'm' (so that math functions can be called...
# ... as 'm' instead of 'math')

print("Welcome to the School Yearbook Efficiency Calculator!")
# Welcomes the user to the program
print("This program will calculate the lowest possible perimeter for your yearbook.")
# Describes how the program functions to satisfy the needs of the user
print("To end this program at anytime, please type 'done' and hit enter.")
# Informs the user to input 'done' at any time if they wish to exit from the program

x = 1
# Conditional value that will force the calculator program to keep repeating as long as x = 1
while x == 1:
# While x is equal to 1, the program for the calculator will keep repeating
    y = 1
    # As long as y=1, user will be prompted/reprompted to enter a valid input for N (line 39)
    while y == 1:
    # While the value of N is undetermined, or a previous input of N is invalid, y will = 1
        N = input("\nPlease enter the number of photos you have: ")
        # Prompts the user to enter the number of photos they have.
        if N == "done" or N == "Done":
        # Condition for if the user indicates that they want to exit the program
            print("Goodbye!")
            # The program will say goodbye to the user
            y = 0
            # y will equal 0 so that the user is not prompted to make another input for N
            x = 0
            # x will equal 0 to exit from the whole program
        else:
        # If the input for N is not 'done' or 'Done' the following program will run...
            N = int(N)
            # The inputted value of N will become an integer
            if N > 0:
            # If N is a positive number greater than 0...
                y = 0
                # ...y will equal to 0, unrequiring the user to enter another valid input of N
            else:
            # If N is less than or equal to 0...
                print("Invalid input. Please enter a positive number greater than 0.")
                # ...the user will be informed that the number they input is invalid
                # Since y still equals 1, the 'while y == 1' loop will repeat
        
    if x == 1:
    # If x == 1, it means that the user wanted the program to continue running
    # If x == 0, it means that the user inputted 'done' for N and wanted the program to end
    # The program would skip running the code in this if statement if x == 0
        factorlist = factors(N)
        # Retrives the factors of the inputted number of N that are less than its square root
        E = len(factorlist) - 1
        # Finds the position of the highest factor within the array of 'factorlist'
        # Because the factors are listed from least to greatest in the array...
        # ...this is used to find the position of the last factor in the array to find the...
        # ...greatest factor out of the factors of N less than or equal to its square root
        D1 = factorlist[E]
        # Sets one of the dimensions as the greatest factor of the 'factorlist' array
        D2 = int(N / Dim1)
        # Divides N by the first dimension to get the second dimension, and then sets the...
        # ...value to an integer to prevent it from being a float
        
        print("Minimum perimeter is %d, with the dimensions %d by %d." %((D1+D2)*2,D1,D2))
        # Prints the most efficient perimeter for the yearbook, given the dimensions D1 & D2.
        #  - Calulcates perimeter given the formula P = 2(l + w) (written as "(D1+D2)*2")
