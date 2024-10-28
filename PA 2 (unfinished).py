"""
Tanvir Rahim
ICS3U
Programming Assignment #2 - Due 11/08/2024
"""


import math as m   # Imports python's math library

def factors(N):   # Defines a function 'factors' that will determine the factors of a number, with the parameter 'N' representing the number in which its factors will be determined
    facs = [1]   # Declares the variable 'facs.' The value of this variable is set to an array consisting of the value '1'. This number is added prerequisitly as all positive numbers have '1' as a factor.
    for i in range(2, m.floor(m.sqrt(N))+1):   # Iterates a range from 2 (1 is already in the facs array) to the square root of N, the number in which its factors will be determined.
        if N % i == 0:   # If the number 'i' is divisible by N with a remainder of 0, it is a factor of N.
            facs.append(i)   # In compliance with the last line of code, the 'i' value will be added onto the array assigned to the variable 'facs'.
    return facs   # Returns the variable 'facs', which will contain an array with a full list of factors oif N, which are less than or equal to the square root of N, to eventually determine the lowest possible perimeter for a School Yearbook when the function is called.

print("Welcome to the School Yearbook Efficiency Calculator!\nThis program will calculate the dimensions of your yearbook which will result in the lowest perimeter possible, through the input of the number of photos you have.\nTo end this program at anytime, please type 'done' and hit enter.")   # Welcomes the user to the program, and describes how the program functions to satisfy the needs of the user. It also informs the user to input 'done' at any time if they wish to exit from the program.

x = 1   # Conditional value that will force the calculator program to keep repeating as long as x = 1.
while x == 1:   # While x is equal to 1, the program for the calculator will keep repeating.
    y = 1   # Conditional value that will eventually equal to '0' once a valid number of photos or 'done' is inputted by the user.
    while y == 1:   # While the value of N is either invalid when inputted, or is undetermined, y will always equal 1.
        N = input("\nPlease enter the number of photos you have: ")   # Prompts the user to enter the number of photos they have.
        if N == "done" or N == "Done":   # Condition for if the user inputs 'done' or 'Done' (indicating that the user would like to exit from the program)
            print("Goodbye!")   # The program will say goodbye to the user.
            y = 0   # Since a valid input is entered for N, y will equal to 0 so that the user will not be required to enter another input for N.
            x = 0   # Since the user wants to end the program, setting x to 0 will stop the program from executing.
        else:   # If the input for N is not 'done,' the following program will run.
            N = int(N)   # The inputted value of N will become an integer.
            if N > 0:   # If N is a positive number greater than 0...
                y = 0   # ...y will equal to 0, which will unrequire the user to enter another "valid" input of N.
            else:   # If N is less than or equal to 0...
                print("%d is an invalid number. Please enter a positive number greater than 0." %N)   # ...the user will be informed that the number they input is invalid, and that they need to enter a positive number greater than 0. Since y is still equal to 1, the 'while y == 1' loop will repeat, meaning that the user will again be prompted to enter an input for N.
        
    if x == 1:   # If x == 1, it means that the user did not input 'done' for the value N, and wanted the program to continue running. If x == 0, it means that the user inputted 'done' for the value N, and wanted the program to end. This means that, if the user inputted 'done,' the program will skip running the code within this if statement.
        factorlist = factors(N)
        E = len(factorlist) - 1
        Dim1 = factorlist[E]
        Dim2 = int(N / Dim1)
    
        print("The smallest possible perimeter is %d, with the dimensions %d by %d." %((Dim1+Dim2)*2,Dim1,Dim2))
