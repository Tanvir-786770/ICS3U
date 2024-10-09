def add(a, b):
  
  
  return a + b
print(add("ONE", "TWO"))

num = 1

x = ""

while (x != "Whole" or x != "whole" or x != "Decimal" or x != "decimal"):
  x = input("Is your first number a whole number, or a decimal number? (Write 'Whole' or 'Decimal')")
  if (x == "Whole" or x == "whole" or x == "Decimal" or x == "decimal"):
    print()
  else:
    print("Invalid input. Try again.")

while (num == 1):
  try:
   a = int(input("Please enter a number: "))
   num = 0
  except:
    num = 1
    print("Invalid input. Try again.")
    
while (ininstance(b, str)):
  b = int(input("Please enter another number: "))
  if isinstance(b, str):
    print("Invalid input. Try again.")
