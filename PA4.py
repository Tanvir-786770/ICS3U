"""
Tanvir Rahim
Programming Assignment 4
Due 12/20/2024

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
# Assigns the string 'wordle.dat' to the variable 'filename.' This is the name of the wordle
# ...data file.
fh = open(filename, 'r')
# Opens the file as 'read-only,' and assigns all file handling actions to the variable 'fh.'

wordarray = []
# Declares an array 'wordarray' as a blank array.
datearray = []
# Declares an array 'datearray' as a blank array.

for r in range(1038):
# Iterating r from 1 to 1038, the following will occur for each step of r.
    line = fh.readline()
    # Reads the first line of the file, and assigns its content as a string value to 'line.'
    line = line.strip()
    # Removes the carriage return from the content in variable 'line' and reassigns the new
    # ...value back into 'line.'
    m, d, y, w = line.split()
    # Splits the different segments of the line of data in 'line,' and assigns these pieces
    # ...of data to the variables 'm' (for month), 'd' (for day), 'y' (for year), and 'w'
    # ...(for the word) respectively.
    date = merge(d, m, y)
    # Calls the merge() function with parameters 'd,' 'm,' and 'y' and assigns the returned
    # ...integer value of the full date to the variable 'date.'
    wordarray.append(w)
    # Appends the value of 'w' onto the array 'wordarray.'
    datearray.append(date)
    # Appends the value of 'date' onto the array 'datearray.'

print("Welcome to the Wordle Database!")
# A print statement welcoming the user to the program.

x = 0
# Declares that x = 0.
while x == 0:
# As long as x is equal to 0, the following will recur.
    g = 0
    # Declares that  g = 0.
    while g == 0:
    # As long as g is equal to 0, the following will recur.
        searchtype = input("\nEnter 'w' to look for a word, or 'd' to look for a date: ")
        # Prompts the user to choose whether or not they would like to search for a word,
        # or a date in this program, and assigns the input to the variable 'searchtype.'
        searchtype = searchtype.lower()
        # Sets all characters of the string value of 'searchtype' as their lowercase
        # ...versions, and then reassigns the new string back into 'searchtype.'

        if searchtype == 'w' or searchtype == 'd':
        # If the value of 'searchtype' is "w" or "d," the following will occur.
            g = 1
            # The variable 'g' will be equal to 1. This will unrequire the user from
            # ... having to make another valid input for the variable 'searchtype.' 
        else:
        # If the value of 'searchtype' is NOT "w" or "d," the following will occur.
            print("Invalid input; try again.")
            # Informs the user that they entered an invalid input, and to try again.
            # -- From this point, the 'while g == 0' loop will repeat and reprompt the
            #    ...user to enter a valid input for 'searctype.'
            


    if searchtype == "w":
    # If the input for 'searchtype' was "w," the following will occur.
        sort(wordarray, datearray, 1)
        # Call the 'sort()' subroutine, given the arrays 'wordarray' and 'datearray.'
        # -- The '1' as the third parameter indicates that the subroutine should sort
        #    ...these arrays in alphabetical order of the words.
        word = input("Enter the word you are looking for: ")
        # Prompts the user to enter the word that they are looking for, and assigns
        # ...the input to variable 'word.'
        word = word.upper()
        # Sets the value of 'word' so that all characters are uppercase, and assigns
        # ...the new string back into 'word.'
        result = isMatch(wordarray, 0, len(wordarray)-1, word)
        # Call the function isMatch(), given the array to search through ('wordarray')
        # ...the lowest index (0), the highest index (1 less than length of wordarray),
        # ...and the word to look for (the string value of 'word'). The return value is
        # ...assigned to the variable 'result.'
        if result == 0:
        # If the value of 'result' is 0 (meaning the word was not found), the following
        # ...will occur.
            print(word, "was not found in this database.")
            # Informs the user that the word they inputted was not found in the
            # ...database.
        else:
        # If the value of 'result' is NOT 0 (meaning that the value of 'result' is the
        # ...date in which the word was used in Wordle), the following will occur.
            print("The word '%s' was the solution to the puzzle on %d." %(word, result))
            # Informs the user that the word was found in the database, and was the
            # ...solution to Wordle on a date, given by the value of 'result.'
            
    

    else:
        sort(wordarray, datearray, 2)
         # Call the 'sort()' subroutine, given the arrays 'wordarray' and 'datearray.'
        # -- The '2' as the third parameter indicates that the subroutine should sort
        #    ...these arrays in chronological order of the dates.
        p = 0
        # Declares the variable 'p' is assigned the integer 0.
        while p == 0:
        # As long as the value of 'p' is 0, the following will recur.
            f = 0
            # Declares the variable 'f' is assigned the integer 0.
            while f == 0:
            # As long as the value of 'f' is 0, the following will recur.
                try:
                # The system will try the following.
                    year = int(input("Enter the year: "))
                    # The user will be prompted to enter the year of the date they are
                    # ...trying to search a word from. The input is assigned as an
                    # ...integer to the variable 'year.'
                    f = 1
                    # f will equal 1, which will unrequire the user to enter a valid
                    # ...input for 'year,' unless an exception is thrown.
                except:
                # If an exception is thrown while determining the value of 'year,' the
                # ...following will occur.
                    print("Invalid input; try again.")
                    # Informs the user that they made an invalid input for 'year,' and
                    # ...that they need to try again.
                    f = 0
                    # f will equal 0, which will cause the while loop to recur,
                    # ...reprompting the user to enter a valid input for 'year.'
        
            year = str(year)
            # Sets the value of 'year' as a string, and reassigns the new string back
            # ...into the variable 'year.'
            t = 0
            # Declares the variable 't' is assigned the integer 0.
            while t == 0:
            # As long as t = 0, the following will occur.
                month = input("Enter the month (3-letter abbreviation; ex: 'Jan'): ")
                # The user will be prompted to enter the month of the date they are
                # ...trying to search a word from. The input is assigned to the
                # ...variable 'month.'
                if month == 'Jan' or month == 'Feb' or month == 'Mar' or month == 'Apr':
                # If the value of 'month is "Jan," "Feb," "Mar," or "Apr," the following
                # ...will occur.
                    t = 1
                    # The value of 't' will be 1, unrequiring the user to enter another
                    # ...valid input for 'month.'
                elif month == 'May' or month == 'Jun' or month == 'Jul' or month == 'Aug':
                # If the value of 'month is "May," "Jun," "Jul," or "Aug," the following
                # ...will occur.
                    t = 1
                    # The value of 't' will be 1, unrequiring the user to enter another
                    # ...valid input for 'month.'
                elif month == 'Sep' or month == 'Oct' or month == 'Nov' or month == 'Dec':
                # If the value of 'month is "Sep," "Oct," "Nov," or "Dec," the following
                # ...will occur.
                    t = 1
                    # The value of 't' will be 1, unrequiring the user to enter another
                    # ...valid input for 'month.'
                ## Although the if/elif statements could have been combined into a single
                ## ...if statement, I seperated them into three statements to avoid the
                ## ...code to extend all the way to the right and stay within the 95
                ## ...column limit for this course.
                else:
                # If the value of 'month' is not a valid three-letter abbreviation for a
                # ...month, the following will occur.
                    print("Invalid input; try again.")
                    # Informs the user that they have made an invalid input for 'month,'
                    # ...and that they must try again.
                    # -- At this point, the 'while t == 0' loop will recur, which will
                    #   ...reprompt the user to enter a valid input for 'month.'
            h = 0
            # Declare the variable 'h' is assigned the integer 0.
            while h == 0:
            # As long as the value of 'h' is 0, the following will recur.
                try:
                # The system will try the following.
                    day = int(input("Enter the day: "))
                    # The user will be prompted to enter a day of a month, and the
                    # ...input will be assigned as an integer to the variable 'day.'
                    if day >= 1 and day <= 31:
                    # If the value of 'day' is greater than or equal to 1 AND less than
                    # ...or equal to 31, the following will occur.
                        h = 1
                        # The value of 'h' will become 1, unrequiring the user to enter
                        # ...another input for 'day' unless an exception is thrown below.
                    else:
                    # If the value of 'day' is NOT between 1 and 31, the following will
                    # ...occur.
                        print("Invalid input; try again.")
                        # The user will be informed that their input for 'day' is invalid.
                        # -- At this point, the 'while h == 0' loop will recur,
                        #   ...reprompting the user to make a valid input for 'day.'
                except:
                    print("Invalid input; try again.")
                    # The user will be informed that their input for 'day' is invalid.
                    # -- At this point, the for 'while h == 0' loop will recur,
                    #    ...reprompting the user to make a valid input for 'day.'

            day = str(day)
            # Sets the value of 'day' as a string, and reassigns the new string back into the
            # ...variable 'day.'
            if int(day) < 10:
            # If the value of 'day,' as an integer, is less than 10, the following will occur:
                day = "0" + day
                # A 0 will be added to the left of the single digit value of 'day,' so that all
                # ...days are in two-digit format, since all dates have two digits for the day.
            dateinput = merge(day, month, year)
            # Calls the function merge(), and gives the values of 'day,' 'month,' and 'year'.
            # ...The return value will be assigned to variable 'dateinput.'
            if dateinput < 20210619:
            # If the value of 'dateinput' is less than 20210619, the following will occur.
                print("No wordles occurred before 20210619. Enter a later date.")
                # The user will be informed that no wordles occurred before June 19, 2021, in
                # ...the database, and that the user will need to enter a later date.
                # -- Since p is still equal to 0, the 'while p == 0' loop will recur, which
                #    ...will reprompt the user to make inputs for variables 'year,' 'month,'
                #    ...and 'day.'
            elif dateinput > 20240421:
            # If the value of 'dateinput' is greater than 20240421, the following will occur.
                print("The last wordle on this database is on 20240421. Try an earlier date.")
                # The user will be informed that no wordles occurred after April 4, 2024, in
                # ...the database, and that the user will need to enter a later date.
                # -- Since p is still equal to 0, the 'while p == 0' loop will recur, which
                #    ...will reprompt the user to make inputs for variables 'year,' 'month,'
                #    ...and 'day.'
            else:
                result = isMatch(datearray, 0, len(datearray)-1, dateinput)
                # Call the function isMatch(), given the array to search through ('datearray')
                # ...the lowest index (0), the highest index (1 less than length of datearray),
                # ...and the date to look for (the value of 'dateinput'). The return value is
                # ...assigned to the variable 'result.'
                print("The solution for the puzzle on", dateinput, "is %s." %result)
                # Informs the user of the word that was the solution to wordle on the given
                # ...date (value of 'dateinput').
                p = 1
        
    c = 0
    # Declares the variable 'c' is assigned the integer 0.
    while c == 0:
    # As long as c is equal to 0, the following will recur.
        cont = input("To run this program again, enter 'r'. To end this program, enter 'e': ")
        # Prompts the user to choose whether they would like to run the program again, or end
        # ...the program. The input is assigned to the variable 'cont.'
        if cont.lower() == 'r':
        # If the value of 'cont,' in all lowercase, is "r," the following will occur.
            c = 1
            # The value of 'c' will be 1, which will prevent the user from entering another
            # ...valid input for 'cont.'
            # -- Since x is still equal to 0, the 'while x == 1' loop will recur, which will
            #    ...run this program again.
        elif cont.lower() == 'e':
        # If the value of 'cont,' in all lowercase, is "r," the following will occur.
            c = 1
            # The value of 'c' will be 1, which will prevent the user from entering another
            # ...valid input for 'cont.'
            x = 1
            # Since x is equal to 1, the 'while x == 1' loop will end, which will prevent the
            # ...program from running again.
        else:
            print("Invalid input; try again.")
            # Informs the user that they have made an invalid input, and that they will have to
            # ...try again.
            # -- Since c is still equal to 0, the 'while c == 1' loop will recur, which will
            #    ...reprompt the user to enter a valid input for 'cont.'

print("\nThank you for using this program!")
# Thanks the user for using the program.
