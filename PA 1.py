"""
Tanvir Rahim
786770
ICS3U0 - Programming Assignment 1
09/24/2024 (Due 10/01/2024)
"""

import math    # Imports the math library

# Part 1: Rectangle

print("I will now calculate the area of a rectangle.")    # Informs the user that the program will calculate the area of a rectangle.
L = float(input("Please enter the length of the rectangle: "))   # Prompts the user to input the length of the rectangle, and assigns the input to L.
W = float(input("Please enter the width of the rectangle: "))   # Prompts the user to input the length of the rectangle, and assigns the input to W.
A = L * W   # Calculates the area of the rectangle, given the formula A = L * W, and assigns the new value to A.
print("When the length of the rectangle is", L, "units, and its width is", W, "units, the area of the rectangle is %.2f units squared." %A)    # Prints what the area of the rectangle is, given the L (length) and W (width) values.


# Part 2: Area of a Circle

print("\nI will now calculate the area of a circle.")    # Informs the user that the program will calculate the area of a circle (the \n creates a new paragraph).
r = float(input("Please enter the radius of the circle: "))   # Prompts the user to input the radius of the circle, and assign the input to r.
A = math.pi * math.pow(r, 2)    # Calculates the area of the circle, given the formula A = pi * r^2, and assigns the new value to A (replaces the value of A from Part 1).
print("When the radius of the circle is", r, "units, the area is %.2f units squared." %A)    # Prints what the area of the circle is, given the r (radius) value.


# Part 3: SA & Volume of a Cylinder

print("\nI will now calculate the volume and surface area of a cylinder.")    # Informs the user that the program will calculate the volume and surface area of a cylinder (the \n creates a new paragraph).
r = float(input("Please enter the radius of the cylinder: "))    # Prompts the user to input the radius of the cylinder, and assigns the input to r (replaces the value of r from Part 2).
h = float(input("Please enter the height of the cylinder: "))    # Prompts the user to input the height of the cylinder, and assigns the input to h.
V = math.pi * math.pow(r, 2) * h    # Calculates the volume of the cylinder, given the formula V = pi * r^2 * h, and assigns the new value to V.
SA = 2 * math.pi * r * h + 2 * math.pi * math.pow(r, 2)    # Calculates the surface area of the cylinder, given the formula SA = pi * r^2 * h, and assigns the new value to SA.
print("When the radius of the cylinder is", r, "units, and the height is", h, "units, the volume of the cylinder is %.2f units cubed, and the surface area is %.2f units squared" %(V,SA))    # Prints what the volume and surface area of the cylinder is, given the r (radius) and h (height) values.


# Part 4: Pendulum

print("\nI will now calculate the time period of a pendulum.")    # Informs the user that the program will calculate the time period of a pendulum (the \n creates a new paragraph).
L = float(input("Please enter the length of the pendulum, in meters: "))    # Prompts the user to enter the length of the pendulum, in meters (replaces the value of L from Part 1).
g = float(9.8)    # Assigns the variable, g (gravity), to 9.8.
P = 2 * math.pi * math.sqrt(L/g)    # Calculates how long it takes for the pendulum to make one back-and-forth swing, given the formnula P = 2 * pi * sqrt of L/g.
print("When the length of the pendulum is", L, "meters, it takes %.2f seconds for the pendulum to make one back-and-forth swing." %P)    # Prints the time, in seconds, that it takes for the pendulum to make one back-and-forth swing, given the L (length) value.
