"""
Tanvir Rahim
Programming Assignment 4
Due 12/19/2024

Variable Dictionary:
    filename - Contains the string value of the name of the wordle data file.
    fh - A 'file handler' that allows the program to access the content of the file being
         accessed.
    wordarray - An array containing all the past solutions to the wordle puzzle. These words
                are extracted from the wordle data file.
    datearray - An array containing all the past dates of wordle puzzles These dates are
                extracted from the wordle data file.
    line - Represents a line of text read from a file (in this case, the wordle data file).
    m - Represents the three-letter abbreviation of a month of a date when a line of text is
        read from the wordle data file.
    d - Represents a day of a month in a datewhen a line of text is read from the wordle data
        file.
    y - Represents a day of a month when a line of text is read from the data file.
    w - Represents a word corresponding to a particular date when a line of text is read from
        the data file. This word is appended into the 'wordarray' array.
    date - The integer value of a date in which a wordle puzzle has occurred, given the values
           of m, d, and y when the merge() function is called.
    x - A conditional value that is equal to the integer 0 until the user chooses to end this
        program
    g - A conditional value that is equal to the integer 0 until the user validly inputs what
        kind of search they want the program to execute (search by word or search by date)
    searchtype - Contains an input from the answer stating if they are looking for a particular
                 word, or a word on a particular date.
    word - Contains the string value of the word that the user is searching for.
    result - Contains the return value when the isMatch() function is called. 
    p - A conditional value equal to the integer 0 until the user inputs a valid date (which
        requires it to be between June 19, 2021 (20210619) and April 21, 2024 (20240421).
    f - A conditional value equal to the integer 0 until the user inputs a valid input for the
        variable 'year.'
    year - A variable containing the year that is part of the date that the user would like
           the program to search for.
    t - A conditional value equal to 0 until the user enters a valid input for the variable
        'month.'
    month - A variable containing the month, that is part of the date that the user would like
            the program to look for, in the form of its three-letter abbreviation.
    h - A conditional value equal to 0 until the user enters a valid input for the variable
        'day.'
    day - A variable containing the day of the month that is part of the date that the user
          would like the program to look for.
    dateinput - A variable containing the integer value of the date the user is searching for,
                given the inputs the user made for the variables 'year,' 'month,' and 'day.'
    c - A conditional value that is equal to 0 until the user makes a valid input on whether
        they want to run the program again, or exit the program.
    cont - A variable containing the input from the user when answering whether they want to
           run the program again, or exit the program.
    
"""

def swap(B, p, q):
# Defines the subroutine 'swap() with paramters 'B' as the array, and then 'p' and 'q' as the
# ...indexes of the values being swapped in the array.
    temp = B[p]
    # Assigns the value of index 'p' in array 'B' to the variable 'temp.'
    B[p] = B[q]
    # Assigns the value of index 'q' to index 'p' in array 'B.'
    B[q] = temp
    # Assigns the value of temp (the previous value of index 'p') to index 'q' in array 'B.'

def sort(wordarr, datearr, a):
# Defines the subroutine 'sort()' with parameters 'wordarr' and 'datearr' as the arrays for
# ...the lists of words and dates from the wordle data file, and then 'a' as an indicator for
# if the words and dates should be sorted in alphabetical order for the words or in
# ...chronological order for the dates.
    if a == 1:
    # If the value of a = 1 (the user wants the lists sorted in alphabetical order for the
    # ..words), the following will occur.
        for i in range(0, len(wordarr) - 1):
        # Iterate i from 0 to 1 less of the length of array 'wordarr.'
            for j in range(i+1, len(wordarr) - 1):
            # Iterate j from i + 1 to 1 less of the length of array 'wordarr.'
                if (wordarr[i] > wordarr[j]):
                # If index i of array 'wordarray' is greater than index j, the following will
                # ...occur.
                    swap(wordarr, i, j)
                    # Call function swap(), with array 'wordarr' and the relevant indexes 'i'
                    # ...and 'j.'
                    swap(datearr, i, j)
                    # Call function swap(), with array 'datearr' and the relevant indexes 'i'
                    # ...and 'j.'
                    # -- Values of the array 'datearr' are being swapped to ensure that the
                    #    ...the dates are in the same indexes as their corresponding words in
                    #    ...the array 'wordarr.'
                    
    elif a == 2:
    # If the value of a = 2 (the user wants the lists sorted in chronological order for the
    # ..dates), the following will occur.
        for i in range(0, len(datearr) - 1):
        # Iterate i from 0 to 1 less of the length of array 'datearr.'
            for j in range(i+1, len(datearr) - 1):
            # Iterate j from i + 1 to 1 less of the length of array 'wordarr.'
                if (datearr[i] > datearr[j]):
                # If index i of array 'datearr' is greater than index j, the following will
                # ...occur.
                    swap(datearr, i, j)
                    # Call function swap(), with array 'datearr' and the relevant indexes 'i'
                    # ...and 'j.'
                    swap(wordarr, i, j)
                    # Call function swap(), with array 'wordarr' and the relevant indexes 'i'
                    # ...and 'j.'
                    # -- Values of the array 'wordarr' are being swapped to ensure that the
                    #    ...the words are in the same indexes as their corresponding dates in
                    #    ...the array 'datearr.'

def merge(p, q, r):
# Defines a function merge() with parameters 'p' as the day, 'q' as the month, and 'r' as the
# ...year.
    if q == "Jan":
    # If the value of q is "Jan," the following will occur.
        q = "01"
        # q will be reassigned the string value of "01."
    elif q == "Feb":
    # If the value of q is "Feb," the following will occur.
        q = "02"
        # q will be reassigned the string value of "02."
    elif q == "Mar":
    # If the value of q is "Mar," the following will occur.
        q = "03"
        # q will be reassigned the string value of "03."
    elif q == "Apr":
    # If the value of q is "Apr," the following will occur.
        q = "04"
        # q will be reassigned the string value of "04."
    elif q == "May":
    # If the value of q is "May," the following will occur.
        q = "05"
        # q will be reassigned the string value of "05."
    elif q == "Jun":
    # If the value of q is "Jun," the following will occur.
        q = "06"
        # q will be reassigned the string value of "06."
    elif q == "Jul":
    # If the value of q is "Jul," the following will occur.
        q = "07"
        # q will be reassigned the string value of "07."
    elif q == "Aug":
    # If the value of q is "Aug," the following will occur.
        q = "08"
        # q will be reassigned the string value of "08."
    elif q == "Sep":
    # If the value of q is "Sep," the following will occur.
        q = "09"
        # q will be reassigned the string value of "09."
    elif q == "Oct":
    # If the value of q is "Oct," the following will occur.
        q = "10"
        # q will be reassigned the string value of "10."
    elif q == "Nov":
    # If the value of q is "Nov," the following will occur.
        q = "11"
        # q will be reassigned the string value of "11."
    elif q == "Dec":
    # If the value of q is "Dec," the following will occur.
        q = "12"
        # q will be reassigned the string value of "12."
        
    return int(r+q+p)
    # Returns the values of 'r', 'q', and 'p', combined together side-by-side, then converted
    # ...to an integer.

def isMatch(array, low, high, item):
# Defines a function isMatch(), with the parameters 'array' as the array being searched, 'low'
# ...as the lowest index of the array, 'high' as the highest index, and 'item' as the term
# ...being searched for in the array (either a particular word or date).
    if high >= low:
    # If the value of 'high' is greater than or equal to the value of 'low,' the following will
    # ...occur.
        mid = (high + low) // 2
        # Add up the values of 'high' and 'low', divide the sum by 2, and assign the quotient
        # ...to the variable 'mid.'
        # -- The double slash (//) is meant to round the quotient down to the nearest whole
        # ...number.
        if array[mid] == item:
        # If the value of 'array' at index 'mid' is equal to the value of 'item,' the following
        # ...will occur
            if array == wordarray:
            # If 'array' is the 'wordarray,' the following will occur.
                return datearray[mid]
                # Return the value of 'datearray' at index 'mid.'
            else:
                return wordarray[mid]
                # Return the value of 'wordarray' at index 'mid.'
        elif array[mid] > item:
        # If the value of 'array' at index 'mid' is greater than the value of 'item,' the
        # ...following will occur.
            return isMatch(array, low, mid - 1, item)
            # Call the function isMatch(), with the same parameters except 'high' as the value
            # ...of mid - 1, and then return the value that is returned from this calling.
            # -- This triggers the recursion of the isMatch() function.
        else:
            return isMatch(array, mid + 1, high, item)
            # Call the function isMatch(), with the same parameters except 'low' as the value
            # ...of mid + 1, and then return the value that is returned from this calling.
            # -- This triggers the recursion of the isMatch() function.
    else:
        return 0
        # Return the integer 0.


filename = "wordle.dat"
fh = open(filename, 'r')

wordarray = []
datearray = []

for r in range(1038):
    line = fh.readline()
    line = line.strip()
    m, d, y, w = line.split()
    date = merge(d, m, y)
    wordarray.append(w)
    datearray.append(date)

print("Welcome to the Wordle Database!")

x = 0
while x == 0:
    g = 0
    while g == 0:
        searchtype = input("\nEnter 'w' to look for a word, or 'd' to look find the word for a date: ")
        searchtype = searchtype.lower()

        if searchtype == 'w' or searchtype == 'd':
            g = 1
        else:
            print("Invalid input; try again.")


    if searchtype == "w":
        sort(wordarray, datearray, 1)
        word = input("Enter the word you are looking for: ")
        word = word.upper()
        result = isMatch(wordarray, 0, len(wordarray)-1, word)
        if result == 0:
            print(word, "was not found in this database.")
        else:
            print("The word '%s' was the solution to the puzzle on %d." %(word, result))
    

    else:
        sort(wordarray, datearray, 2)
        p = 1
        while p == 1:
            f = 0
            while f == 0:
                try:
                    year = int(input("Enter the year: "))
                    f = 1
                except:
                    print("Invalid input; try again.")
                    f = 0
        
            year = str(year)
            t = 0
            while t == 0:
                month = input("Enter the month (3-letter abbreviation; ex: 'Jan'): ")
                if month == 'Jan' or month == 'Feb' or month == 'Mar' or month == 'Apr':
                    t = 1
                elif month == 'May' or month == 'Jun' or month == 'Jul' or month == 'Aug':
                    t = 1
                elif month == 'Sep' or month == 'Oct' or month == 'Nov' or month == 'Dec':
                    t = 1
                else:
                    print("Invalid input; try again.")
            h = 0
            while h == 0:
                try:
                    day = int(input("Enter the day: "))
                    if day >= 1 and day <= 31:
                        h = 1
                    else:
                        print("Invalid input; try again.")
                except:
                    print("Invalid input; try again.")

            day = str(day)
            if int(day) < 10:
                day = "0" + day
            dateinput = merge(day, month, year)
            if dateinput < 20210619:
                print("No wordles occurred before 20210619. Enter a later date.")
            elif dateinput > 20240421:
                print("The latest wordle on this database is on 20240421. Enter an earlier date.")
            else:
                result = isMatch(datearray, 0, len(datearray)-1, dateinput)
                print("The solution for the puzzle on", dateinput, "is %s." %result)
                p = 0
        
    c = 0
    while c == 0:
        cont = input("To run this program again, enter 'r'. To end this program, enter 'e': ")
        if cont.lower() == 'r':
            c = 1
        elif cont.lower() == 'e':
            c = 1
            x = 1
        else:
            print("Invalid input; try again.")

print("Thank you for using this program!")
