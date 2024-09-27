import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
if (x > 0 and x <= 20):
  y = input("Please input another nonzero whole number")
  y = int(y)
  if (y != 0):
    print("Now deciding if", y, "is a factor of", x, "...")
    rem = x % y
    if rem == 0:
      print("Yes!", y, "is a factor of", x)
    else:
      print(y, "is not a factor of", x)
  else:
    print("You are not allowed to input zero. A factor could not be determined.")
else:
  print(x, "is out of range. Please try again.")
