"""
Tanvir Rahim
ICS3U - Programming Assignment 3
Due 12/06/2024

Variable Dictionary:

    t - Variable representing the turtle library.
    yn - A value of 0 that does not change to 1 until the user inputs a valid yes/no answer.
    ans - A variable that is assigned an inputted yes/no string value when the user is
            prompted to answer a question.
    bgcolor - A variable containing the name of the background color of the turtle graphics
                plotter as a string.
    xcord - The x-coordinate that the turtle plotter will move to in order to plot a point.
    ycord - The y-coordinate that the turtle plotter will move to in order to plot a point.
    d - The unit size of the point that will be plotted by turtle.
    color - A certain color that the image has. This is referenced by the turtle plotter
            in order for it to plot points with the right color.
    f - A conditional value that does not change until the user inputs a valid file name.
    filename - The name of the file that the program will read.
    fh - The file handler; it is used for certain functions such as reading a line of the
            file.
    imageData - Contains information about the number of colors in the image, as well as the
                number of columns and rows the image has in the data file.
    cols - Value representing the number of columns the image has in the data file.
    rows - Value representing the number of rows the image has in the data file.
    numColors - Value representing the number of colors the image has.
    myColors - A dictionary containing information about the symbols in the image data file
                and the colors that they represent.
    line - Represents a line of text in the data file.
    sym - The symbol in the image data file that represents a certain color of the image.
    c - The letter in the image data file that seperates the symbol from its corresponding
        color. (It is simply used to get rid of itself).
    imagearray - An array containing the actual data of the image (a whole bunch of symbols
                    written out to actually form the image through text). These symbols
                    represent a certain color of the image (the variable 'sym').
    rotation - A variable containing a yes/no answer, as a string, to a prompt asking the user if
                they would like the image rotated.
    rc - A value of 0 that does not change to 1 until the user inputs a valid response to
            what kind of rotation they would like (90/180/270).
    rchoice - A variable containing the answer to a prompt asking the user what kind of rotation
                they want.
    lightbg - A variable containing a yes/no answer, as a string, to a prompt asking the user if
                they would like a lighter background (gray70) or keep it at default (gray40).
    x - The variable that iterates through the number of columns of an image; it represents an
        x coordinate of a particular symbol representing a point on the image in the data file.
    y - The variable that iterates through the number of columns of an image; it represents a
        y coordinate of a particular symbol representing a point on the image in the data file.
"""

import turtle as t
# Imports the Turtle Library and assigns it to 't'.

def ynprompt(question):
# Defines a function that prompts the user a yes/no question and expects a yes/no answer.
# The paramter is the question that the user will be asked.
    yn = 0
    # As long as yn = 0, the user will be prompted with the question again until a valid
    # ...yes/no response is received.
    while yn == 0:
    # The following loop will occur as long as yn = 0.
        ans = input("%s [Y/N]: " %question)
        # Prompts the user with the question, and informs the user in a bracketed box that
        # ...the user can either respond with 'Y' or 'N'. The response is saved in the
        # ...'ans' variable.
        if ans == 'Y' or ans == 'y' or ans == 'N' or ans == 'n':
        # If the answer provided to the prompted question is 'Y'/'y' (yes) or 'N'/'n' (no),
        # ...the following will occur.
            yn = 1
            # The value of yn will be set to 1, meaning the while loop will end.
        else:
        # If the answer provided to the prompted question is NOT a Y/N response, the
        # ...following will occur.
            print("Invalid input; try again.")
            # Lets the user know that the input is invalid, as it is not a Y/N answer.
    return ans
    # Returns the value of 'ans', which is expected to either be 'Y'/'y' or 'N'/'n'.

def turtlesetup(bgcolor):
# Defines a subroutine that will set up the turtle plotter.
# The parameter is the background color of the turtle plotter that the user chooses.
    t.hideturtle()
    # Hides the turtle pointer/plotter from the screen to avoid obstruction of viewing
    # ...the actual image.
    t.penup()
    # Lifts the turtle plotter from the canvas.
    t.bgcolor(bgcolor)
    # Sets the background color to a certain gray background that the user chooses, which
    # ...is represented by 'bgcolor'
    t.tracer(0, 0)
    # Prevents the turtle plotter from displaying any actions (this speeds up the process
    # ...of plotting the image on turtle).
    # Later, the 'turtle.update()' function is executed, which updates the canvas after
    # ...the entire image is plotted.
  
def plotitUpright(cols, rows, x, y, d, color):
# Defines a subroutine that plots a point when the image being plotted will be oriented
# ...upright.
    xcord = (-(cols/2)+x) * 2
    # The x-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the x-value of the image in its data value.
    ycord = ((rows/2)-y) * 2
    # The y-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the y-value of the image in its data value.
    t.goto(xcord, ycord)
    # The turtle plotter will move its posiition to the x/y coordinates given, which are
    # ...the values of 'xcord' and 'ycord'.
    t.pendown()
    # Sets the turtle plotter onto the canvas.
    t.dot(d, color)
    # Plots a dot, with 'd' representing the size of the dot, and 'color' representing
    # ...the color of the dot.
    t.penup()
    # Lifts the turtle plotter up from the canvas.
    
def plotitUpsidedown(cols, rows, x, y, d, color):
# Defines a subroutine that plots a point when the image being plotted will be oriented
# ...upside-down.
    xcord = (-(cols/2)+x) * 2
    # The x-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the x-value of the image in its data value.
    ycord = ((rows/2)-y) * 2
    # The y-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the y-value of the image in its data value.
    t.goto(-(xcord), -(ycord))
    # The turtle plotter will move its posiition to the x/y coordinates given, which are
    # ...the values of 'xcord' and 'ycord'.
    # (The xcord and ycord values are switched from (x, y) to (-x, -y) in order to comply
    # ...with an upside-down orientation of the image.)
    t.pendown()
    # Sets the turtle plotter onto the canvas.
    t.dot(d, color)
    # Plots a dot, with 'd' representing the size of the dot, and 'color' representing
    # ...the color of the dot.
    t.penup()
    # Lifts the turtle plotter up from the canvas.

def plotit90deg(cols, rows, x, y, d, color):
# Defines a subroutine that plots a point when the image being plotted will be oriented
# ...90 degrees clockwise.
    xcord = (-(cols/2)+x) * 2
    # The x-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the x-value of the image in its data value.
    ycord = ((rows/2)-y) * 2
    # The y-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the y-value of the image in its data value.
    t.goto(ycord, -(xcord))
    # The turtle plotter will move its posiition to the x/y coordinates given, which are
    # ...the values of 'xcord' and 'ycord'.
    # (The xcord and ycord values are swapped from (x, y) to (y, -x) in order to comply
    # ...with a 90 degree clockwise orientation of the image.)
    t.pendown()
    # Sets the turtle plotter onto the canvas.
    t.dot(d, color)
    # Plots a dot, with 'd' representing the size of the dot, and 'color' representing
    # ...the color of the dot.
    t.penup()
    # Lifts the turtle plotter up from the canvas.
    
def plotit270deg(cols, rows, x, y, d, color):
# Defines a subroutine that plots a point when the image being plotted will be oriented
# ...270 degrees clockwise.
    xcord = (-(cols/2)+x) * 2
    # The x-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the x-value of the image in its data value.
    ycord = ((rows/2)-y) * 2
    # The y-coordinate on the turtle canvas that the turtle plotter will plot a point on,
    # ...based on the y-value of the image in its data value.
    t.goto(-(ycord), xcord)
    # The turtle plotter will move its posiition to the x/y coordinates given, which are
    # ...the values of 'xcord' and 'ycord'.
    # (The xcord and ycord values are swapped from (x, y) to (-y, x) in order to comply
    # ...with a 270 degree clockwise orientation of the image.)
    t.pendown()
    # Sets the turtle plotter onto the canvas.
    t.dot(d, color)
    # Plots a dot, with 'd' representing the size of the dot, and 'color' representing
    # ...the color of the dot.
    t.penup()
    # Lifts the turtle plotter up from the canvas.

print("Welcome to the graphics plotter!")
# Welcomes the user to the program.
print("This program will plot an image using an inputted file!")
# Briefly describes what the program will do for the user.

f = 0
# As long as f = 0, the user will be prompted to enter a valid file name that is
# ...valid and should be accessible.
while f == 0:
# The following loop will occur as long as f = 0.
    try:
    # The program will try and execute the following tasks without any errors.
        filename = input("\nTo begin, please enter the name of your '.xpm' file: ")
        # The user is prompted to enter the name of the image data (.xpm) file, and
        # ...the inputted name is assigned as a string to 'filename'
        fh = open(filename, "r")
        # Opens the file that was entered in the above prompt, with "r" setting the
        # ...file access to read-only.
        f = 1
        # The value of f will be 1, meaning that the while loop will end, unless an
        # ...invalid input was made when entering the name of the file, meaning f
        # ...will equal 0 when an exception occurs.
    except:
    # The following tasks will be executed if an exception occurs.
        print("ERROR: File not found! Please try again!")
        # Informs the user that an error has been detected, and that they should try again.
        print("HINT: Try placing the '.xpm' file in the same folder as this python script.")
        # Provides the user with a friendly hint that can possibly resolve the error.
        f = 0
        # Since f = 0, the while loop will repeat, which will reprompt the user to enter a
        # ...valid file name.

imageData = fh.readline()
# Reads the first line of the file, and assigns the content to the variable 'imageData'.
imageData = imageData.strip()
# Used to get rid of the carriage return of this line of content.

cols, rows, numColors = imageData.split()
# Seperates the three values of the imageData line, and assigns the first value (the number
# ...of columns) to 'cols', the second value (the number of rows) to 'rows', and the third
# ...value (the number of colors) to 'numColors'.

rows = int(rows)
# Sets the data type of 'rows' as an integer, and assigns it back to the variable 'rows'.
cols = int(cols)
# Sets the data type of 'cols' as an integer, and assigns it back to the variable 'cols'.
numColors = int(numColors)
# Sets the data type of 'numColors' as an integer, and assigns it back to the variable
# ...'numColors'.
print("\nFILE:", filename)
# Prints the name of the file (the \n is meant to break onto another line to leave a space
# ...between this line and the line above in the output console.
print("%d by %d; %d colors." %(rows,cols,numColors))
# Prints out the preliminary information about the image (number of columns, number of rows,
# ...and the number of colors in the image)

myColors = {
    
    }
# Opens a dictionary named 'myColors', where all the information about the symbols in the
# ...data file, and the colors they represent, will be stored.

for n in range(numColors):
# In this for-loop, n is iterated through a range between 1 and the number of colors.
    line = fh.readline()
    # Reads the next line of content in the data file, and assigns that content to 'line'.
    line.strip()
    # Used to get rid of the carriage return of this line of content.
    sym, c, color = line.split()
    # Seperates the three values of the line, and assigns the first value (the symbol) to
    # ...'sym', the second value (the letter c) to 'c', and the third value (the color)
    # ...to 'color'.
    if sym == "~":
    # If the symbol representing a color is '~', the following will occur.
        sym = " "
        # The symbol for that color will be replaced with a space.
        # This is because all tilde symbols actually represent spaces, but are tildes
        # ...instead because python does not detect spaces as a piece of content when it
        # ...reads a file.
    myColors.update({sym:color})
    # Adds a new entry into the myColors dictionary, stating that the symbol represents
    # ...its corresponding color.

imagearray = []
# Declares a blank array named 'imagearray' that will eventually contain the entire 2D
# ...image as symbols that represent their corresponding colors.

for x in range(rows):
    # In this for-loop, x is iterated through a range between 1 and the number of rows.
    line = fh.readline()
    # Reads the next line of content in the data file, and assigns that content to 'line'.
    line.strip()
    # Used to get rid of the carriage return of this line of content.
    line = line.replace('\n', '')
    # Removes the paragraph-break to only get the pure content of the image data only.
    imagearray.append(line)
    # Appends the line (which is a row of the image) into 'imagearray'.

rotation = ynprompt("Would you like your image rotated?")
# Calls the ynprompt() function by asking the user if they would like the image rotated.

if rotation == 'Y' or rotation == 'y':
# If the input for the prompt above is 'Y'/'y', the following will occur.
    rc = 0
    # As long as rc = 0, the user will be prompted to enter a valid response when asked
    # ...how they would like the image rotated in degrees.
    while rc == 0:
    # While rc = 0, the following loop will occur.
        rchoice = int(input("How would you like your image rotated (in degrees)? [90/180/270]: "))
        # The user is asked how they would like the image to be rotated, in degrees. Valid inputs
        # ...are 90, 180, and 270. The inputted number is assigned to 'rchoice' as an integer.
        if rchoice == 90 or rchoice == 180 or rchoice == 270:
        # If a valid input [90/180/270] is made for 'rchoice', the following will occur.
            rc = 1
            # The value of rc will be 1, meaning the loop will end.
        else:
        # If a valid input [90/180/270] is NOT made for 'rchoice', the following will occur.
            print("Invalid input; try again.")
            # The user is informed that an invalid input has been made, and that they need to try
            # ...again.
            # Since rc would still equal 0, the loop will repeat, reprompting the user to enter a
            # ...valid input for 'rchoice'.
            
else:
# If the input for the prompt for 'rotation' is NOT 'Y'/'y', then the following will occur.
    rchoice = 0
    # Since the user does not want a rotation, 'rchoice' will be assigned a value of 0.

print("The background is currently set as 'dark' (gray40).")
# Informs the user that the default background color is 'gray40'.
lightbg = ynprompt("Would you like the 'light' background (gray70) instead?")
# Calls the ynprompt() function by asking the user if they would like the 'gray70' background
# ...instead.

print("\nThe image is now being plotted. Please wait...")
# Informs the user that turtle is now plotting the image, and asks the user for patience while
# ...the plotting process executes.
print("HINT: You will see the image on the 'Python Turtle Graphics' window.")
# Gives a hint to the user, letting them know that the image will be displayed on a seperate
# ..window named 'Python Turtle Graphics'.


if lightbg == 'Y' or lightbg == 'y':
# If the inputted value for 'lightbg' is 'Y'/'y', the following will occur.
    turtlesetup("gray70")
    # The turtlesetup() function is called with the background color set to 'gray70'.
else:
    turtlesetup("gray40")
    # The turtlesetup() function is called with the background color set to 'gray40'.
    
        
if rchoice == 90:
# If the inputted value for 'rchoice' is '90', the following will occur.
    for x in range(cols):
    # In this for loop, 'x' will be iterated through a range of 1 and the number of
    # ...columns the image has in the data file.
        for y in range(rows):
        # In this for loop, 'y' will be iterated through a range of 1 and the number of rows
        # ...the image has in the data file.
            symbol = imagearray[y][x]
            # The program will look for the symbol (logically, the point) of the image
            # ...that is located at certain position of the imagearray given by the 'x'
            # ...and 'y' values. That symbol will be assigned to the variable 'symbol'.
            color = myColors[symbol]
            # The program will look in the dictionary and search for the color represented
            # ...by the symbol. 
            plotit90deg(cols, rows, x, y, 3, color)
            # Calls the plotit90deg() function by giving the number of columns as 'cols',
            # ...the number of rows as 'rows', the values of 'x' and 'y', the size of
            # ...the point to be plotted, and the color of the point as 'color'.

elif rchoice == 180:
# If the inputted value for 'rchoice' is '180', the following will occur.
    for x in range(cols):
    # In this for loop, 'x' will be iterated through a range of 1 and the number of
    # ...columns the image has in the data file.
        for y in range(rows):
        # In this for loop, 'y' will be iterated through a range of 1 and the number of rows
        # ...the image has in the data file.
            symbol = imagearray[y][x]
            # The program will look for the symbol (logically, the point) of the image
            # ...that is located at certain position of the imagearray given by the 'x'
            # ...and 'y' values. That symbol will be assigned to the variable 'symbol'.
            color = myColors[symbol]
            # The program will look in the dictionary and search for the color represented
            # ...by the symbol. 
            plotitUpsidedown(cols, rows, x, y, 3, color)
            # Calls the plotitUpsidedown() function by giving the number of columns as
            # ...'cols', the number of rows as 'rows', the values of 'x' and 'y', the size
            # ...of the point to be plotted, and the color of the point as 'color'.
            
elif rchoice == 270:
# If the inputted value for 'rchoice' is '270', the following will occur.
    for x in range(cols):
    # In this for loop, 'x' will be iterated through a range of 1 and the number of
    # ...columns the image has in the data file.
        for y in range(rows):
        # In this for loop, 'y' will be iterated through a range of 1 and the number of rows
        # ...the image has in the data file.
            symbol = imagearray[y][x]
            # The program will look for the symbol (logically, the point) of the image
            # ...that is located at certain position of the imagearray given by the 'x'
            # ...and 'y' values. That symbol will be assigned to the variable 'symbol'.
            color = myColors[symbol]
            # The program will look in the dictionary and search for the color represented
            # ...by the symbol.
            plotit270deg(cols, rows, x, y, 3, color)
            # Calls the plotit270deg() function by giving the number of columns as 'cols',
            # ...the number of rows as 'rows', the values of 'x' and 'y', the size of
            # ...the point to be plotted, and the color of the point as 'color'.
else:
# If the value for 'rchoice' is '0', the following will occur.
    for x in range(cols):
    # In this for loop, 'x' will be iterated through a range of 1 and the number of
    # ...columns the image has in the data file
        for y in range(rows):
        # In this for loop, 'y' will be iterated through a range of 1 and the number of rows
        # ...the image has in the data file.
            symbol = imagearray[y][x]
            # The program will look for the symbol (logically, the point) of the image
            # ...that is located at certain position of the imagearray given by the 'x'
            # ...and 'y' values. That symbol will be assigned to the variable 'symbol'.
            color = myColors[symbol]
            # The program will look in the dictionary and search for the color represented
            # ...by the symbol.
            plotitUpright(cols, rows, x, y, 3, color)
            # Calls the plotitUpright() function by giving the number of columns as 'cols',
            # ...the number of rows as 'rows', the values of 'x' and 'y', the size of
            # ...the point to be plotted, and the color of the point as 'color'.

print("\nThe image has been plotted. Awaiting canvas update...")
# Informs the user that the image has been fully plotted by turtle, and that the user
# ...should wait for the canvas to be updated.
t.update()
# Updates the turtle canvas with all actions made since the 'turtle.Tracer(0, 0)'
# ...command was executed (this will display the image that turtle plotted).
print("The image has been displayed! Please check the 'Python Turtle Graphics' window!")
# Informs the user that the image has been displayed, and to check the 'Python Turtle
# ...Graphics' window on their computer's taskbar.
print("\nThank you for using this program! :)")
# Thanks the user for using this program.
fh.close()
# Closes the image data file.
