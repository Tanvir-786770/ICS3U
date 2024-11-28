"""
Tanvir Rahim
ICS3U - Programming Assignment 3
Due 12/06/2024
"""


import turtle as t
  
def turtlesetup(bgcolor):
    t.penup()
    t.hideturtle()
    t.bgcolor(bgcolor)
    t.tracer(0, 0)
  
def plotitUpright(cols, rows, x, y, d, color):
    t.penup()
    t.goto((-(cols/2)+x) * 2, ((rows/2)-y) * 2)
    t.pendown()
    t.dot(d, color)
    t.penup()
    
def plotitUpsidedown(cols, rows, x, y, d, color):
    t.penup()
    t.goto(((cols/2)-x) * 2, (-(rows/2)+y) * 2)
    t.pendown()
    t.dot(d, color)
    t.penup()

print("Welcome to the graphics plotter!")
print("This program will plot an image using an inputted file!")

x = 0
while x == 0:
    try:
        x = 1
        filename = input("\nTo begin, please enter the name of your image .txt/.xpm file: ")
        fh = open(filename, "r")
    except:
        print("ERROR: File not found! Please try again!")
        x = 0

colorData = fh.readline()
colorData = colorData.strip()

cols, rows, numColors = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)
print("\nFILE:", filename)
print("%d by %d; %d colors." %(rows,cols,numColors))

u = 0
while u == 0:
    upsidedown = input("\nWould you like your image to be upside down? [Y/N]: ")
    if upsidedown == 'Y' or upsidedown == 'N' or upsidedown == 'y' or upsidedown == 'n':
        u = 1
    else:
        print("Invalid input; try again.")

c = 0
while c == 0:
    Gray = input("Would you like a lighter or darker gray background? [Light/Dark]: ")
    if Gray == 'Light' or Gray == 'Dark' or Gray == 'light' or Gray == 'dark':
        c = 1
    else:
        print("Invalid input; try again.")

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

print("\nThe image is now being plotted. Please wait...")
print("HINT: You will see the image on the 'Python Turtle Graphics' window.")

if Gray == 'Dark' or Gray == 'dark':
    turtlesetup("gray40")
else:
    turtlesetup("gray70")

if upsidedown == 'Y' or upsidedown == 'y':
    for x in range(cols):
        for y in range(rows):
            symbol = imagearray[y][x]
            color = myColors[symbol]
            plotitUpsidedown(cols, rows, x, y, 3, color)
else:
    for x in range(cols):
        for y in range(rows):
            symbol = imagearray[y][x]
            color = myColors[symbol]
            plotitUpright(cols, rows, x, y, 3, color)
    
t.update()        

print("\nThe image has been plotted! Please check the 'Python Turtle Graphics' window!")
fh.close()
