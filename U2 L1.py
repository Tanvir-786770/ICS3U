print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A" or ch == "apples" or ch == "Apples"):
    print("I prefer apples")
elif (ch == "B" or ch == "bananas" or ch == "Bananas"):
    print("I prefer bananas")
elif (ch == "C" or ch == "cherries" or ch == "Cherries"):
    print("I prefer cherries")
else:
    print("You did not choose a valid option!")
    
    
A = B = 10 # How to assign the same thing to multiple variables
C = D = 50
if (A == B) and (C == D): # Example of a compound conditional
    print("Hooray!") # this is what gets printed in this case
else:
    print("Boo!")

g = int(input("Please enter your numeric grade: "))

if (g >= 80 and g <= 100):
  print("You got an A!")
elif (g >= 70 and g < 80):
  print("You got a B!")
elif (g >= 60 and g < 70):
  print("You got a C!")
elif (g >= 50 and g < 60):
  print("You got a D!")
elif (g > 0 and g < 50):
  print("You got an F. :(")
else:
  print("The grade you have inputted is invalid!")
