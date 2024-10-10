import sys
import math as m

def add(a, b):
  
  
  return a + b
print(add("ONE", "TWO"))

num = 1

x = input("Is your first number a whole number or a float? (Write 'Whole' or 'Float'): ")

if (x == "Whole" or x == "whole"):
  while (num == 1):
    try:
      a = int(input("Please enter a number: "))
      num = 0
    except:
      num = 1
      print("Invalid input. Try again.")
      
elif (x == "Float" or x == "float"):
  while (num == 1):
    try:
      a = float(input("Please enter a number: "))
      num = 0
    except:
      num = 1
      print("Invalid input. Try again.")

else:
  print("Invalid input. Restart code.")
  sys.exit()
      
y = input("Is your second number a whole number or a float? (Write 'Whole' or 'Float'): ")

num = 1

if (y == "Whole" or y == "whole"):
  while (num == 1):
    try:
      b = int(input("Please enter a number: "))
      num = 0
    except:
      num = 1
      print("Invalid input. Try again.")
      
elif (y == "Float" or y == "float"):
  while (num == 1):
    try:
      b = float(input("Please enter a number: "))
      num = 0
    except:
      num = 1
      print("Invalid input. Try again.")

else:
  print("Invalid input. Restart code.")
  sys.exit()

new = add(a, b) * 2

print("After adding your two numbers together, and then multiplying the sum by 2, your new number is", new)

def myPow(m, n):
  exnum = m ** n
  return exnum
  
print("Raising your first number to the power of the second number, your next new number is", myPow(a, b))
