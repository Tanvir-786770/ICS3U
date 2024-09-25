import math
length = input("Please input a length: ")
length = float(length)
area = math.pow(length, 2)
print("The area of a square of side length", length, "is:", area)


# Area of a Norman Window Activity

print("Area of a Norman Window shape")
r = float(input("Please input the circle's radius: "))
rSQ = math.pow(r, 2)     # r squared
n = math.pi 
sqarea = rSQ * 4     # area of square
cirarea = n * rSQ * 0.5     # area of semi-circle
areatotal = sqarea + cirarea     # sum of the areas of the square and semi-circle
print("Area is:", areatotal)
