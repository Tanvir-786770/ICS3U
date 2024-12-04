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
    rotation - A variable containing the answer to a prompt asking the user if they would like
                the image rotated.
    rc - A value of 0 that does not change to 1 until the user inputs a valid response to
            what kind of rotation they would like (90/180/270).
    rchoice - A value containing the answer to a prompt asking the user what kind of rotation
                they want.
    
    

"""


import turtle as t

def ynprompt(question):
    yn = 1
    while yn == 1:
        ans = input("%s [Y/N]: " %question)
        if ans == 'Y' or ans == 'y' or ans == 'N' or ans == 'n':
            yn = 0
        else:
            print("Invalid input; try again.")
    return ans

def turtlesetup(bgcolor):
    t.penup()
    t.hideturtle()
    t.bgcolor(bgcolor)
    t.tracer(0, 0)
  
def plotitUpright(cols, rows, x, y, d, color):
    t.penup()
    xcord = (-(cols/2)+x) * 2
    ycord = ((rows/2)-y) * 2
    t.goto(xcord, ycord)
    t.pendown()
    t.dot(d, color)
    t.penup()
    
def plotitUpsidedown(cols, rows, x, y, d, color):
    t.penup()
    xcord = (-(cols/2)+x) * 2
    ycord = ((rows/2)-y) * 2
    t.goto(-(xcord), -(ycord))
    t.pendown()
    t.dot(d, color)
    t.penup()

def plotit90deg(cols, rows, x, y, d, color):
    t.penup()
    xcord = (-(cols/2)+x) * 2
    ycord = ((rows/2)-y) * 2
    t.goto(ycord, -(xcord))
    t.pendown()
    t.dot(d, color)
    t.penup()
    
def plotit270deg(cols, rows, x, y, d, color):
    t.penup()
    xcord = (-(cols/2)+x) * 2
    ycord = ((rows/2)-y) * 2
    t.goto(-(ycord), xcord)
    t.pendown()
    t.dot(d, color)
    t.penup()

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
