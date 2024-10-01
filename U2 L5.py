import math

upper = 5
print("j   tri       factorial")
print("-----------------------")
for i in range(1, upper + 1):
    print("%d   %d         %d" %(i, i**2, math.factorial(i)))
