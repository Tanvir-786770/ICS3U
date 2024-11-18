filename = "file.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()

rows, cols, numColors = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)
print("%d by %d; %d colors." %(rows,cols,numColors))

# Using arrays
colorDefs = [[0] * 2] * numColors # declare the array
for i in range(numColors):
   colorLine = fh.readline() # file handle must be open
   colorLine.strip() 
   sym, c, color = colorLine.split()
   if sym == "~":
       sym = " "
   colorDefs[i][0] = sym
   colorDefs[i][1] = color
   print(colorDefs[i][0], ":", colorDefs[i][1])

print("")
for k in range(rows):
    imagerow = fh.readline()
    print(imagerow, end="")

fh.close()
