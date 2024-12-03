"""
Tanvir Rahim
ICS3U - Programming Assignment 3
Due 12/06/2024

"""


import turtle as t

def ynprompt(question):
    x = 1
    while x == 1:
        ans = input("%s [Y/N]: " %question)
        if ans == 'Y' or ans == 'y' or ans == 'N' or ans == 'n':
            x = 0
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

x = 0
while x == 0:
    try:
        x = 1
        filename = input("\nTo begin, please enter the name of your '.xpm' file: ")
        fh = open(filename, "r")
    except:
        print("ERROR: File not found! Please try again!")
        print("HINT: Try placing the '.xpm' file in the same folder as this python script.")
        x = 0

colorData = fh.readline()
colorData = colorData.strip()

cols, rows, numColors = colorData.split()

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
    q = 0
    while q == 0:
        rchoice = int(input("How would you like your image rotated (in degrees)? [90/180/270]: "))
        if rchoice == 90 or rchoice == 180 or rchoice == 270:
            q = 1
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
