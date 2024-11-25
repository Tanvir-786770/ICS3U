import turtle as t

def plotit(x, y, d, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(d, color)
    t.penup()

filename = "rocky_bullwinkle_mod.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()

rows, cols, numColors = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)
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

t.penup()
t.goto(-(rows/2), cols/2)

t.hideturtle()
t.tracer(0, 0)
print(myColors)
print(imagearray)
for x in range(cols):
    for y in range(rows):
        symbol = imagearray[y][x]
        color = myColors[symbol]
        plotit((-(cols/2)+(x-1)), ((rows/2)-(y+1)), 3, color)
t.update()        

fh.close()
