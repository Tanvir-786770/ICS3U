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
    line - Represents a line of text of the data file.
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
    while yn == 0:   # The following loop will occur as long as yn = 0.
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
print("This program will plot an image using an inputted file!")

f = 0
while f == 0:
    try:
        filename = input("\nTo begin, please enter the name of your '.xpm' file: ")
        fh = open(filename, "r")
        f = 1
    except:
        print("ERROR: File not found! Please try again!")
        print("HINT: Try placing the '.xpm' file in the same folder as this python script.")
        f = 0

imageData = fh.readline()
imageData = imageData.strip()

cols, rows, numColors = imageData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)
print("\nFILE:", filename)
print("%d by %d; %d colors." %(rows,cols,numColors))

myColors = {
    
    }

for n in range(numColors):
    line = fh.readline()
    line.strip()
    sym, c, color = line.split()
    if sym == "~":
        sym = " "
    myColors.update({sym:color})

imagearray = []

for x in range(rows):
    line = fh.readline()
    line.strip()
    line = line.replace('\n', '')
    imagearray.append(line)

rotation = ynprompt("Would you like your image rotated?")

if rotation == 'Y' or rotation == 'y':
    rc = 0
    while rc == 0:
        rchoice = int(input("How would you like your image rotated (in degrees)? [90/180/270]: "))
        if rchoice == 90 or rchoice == 180 or rchoice == 270:
            rc = 1
        else:
            print("Invalid input; try again.")
else:
    rchoice = 0

print("The background is currently set as 'dark' (gray40).")
lightbg = ynprompt("Would you like the 'light' background (gray70) instead?")

print("\nThe image is now being plotted. Please wait...")
print("HINT: You will see the image on the 'Python Turtle Graphics' window.")


if lightbg == 'Y' or lightbg == 'y':
    turtlesetup("gray70")
else:
    turtlesetup("gray40")
        
if rchoice == 90:
    for x in range(cols):
        for y in range(rows):
            symbol = imagearray[y][x]
            color = myColors[symbol]
            plotit90deg(cols, rows, x, y, 3, color)

elif rchoice == 180:
    for x in range(cols):
        for y in range(rows):
            symbol = imagearray[y][x]
            color = myColors[symbol]
            plotitUpsidedown(cols, rows, x, y, 3, color)
            
elif rchoice == 270:
    for x in range(cols):
        for y in range(rows):
            symbol = imagearray[y][x]
            color = myColors[symbol]
            plotit270deg(cols, rows, x, y, 3, color)
else:
    for x in range(cols):
        for y in range(rows):
            symbol = imagearray[y][x]
            color = myColors[symbol]
            plotitUpright(cols, rows, x, y, 3, color)

print("\nThe image has been plotted. Awaiting canvas update...")
t.update()
print("The image has been displayed! Please check the 'Python Turtle Graphics' window!")
print("\nThank you for using this program! :)")
fh.close()
