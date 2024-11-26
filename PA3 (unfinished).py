import turtle as t

def plotit(x, y, d, color):
    t.penup()
    t.goto(x, y)
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
t.penup()
t.hideturtle()
t.tracer(0, 0)
for x in range(cols):
    for y in range(rows):
        symbol = imagearray[y][x]
        color = myColors[symbol]
        plotit((-(cols/2)+(x-1))*2, ((rows/2)-(y+1))*2, 3, color)
t.update()        

print("\nThe image has been plotted! Please check the 'Python Turtle Graphics' window!")
fh.close()
