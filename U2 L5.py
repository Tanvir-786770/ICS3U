import math

n = int(input("Please enter a non-zero whole number: "))
print("j   tri       factorial")
print("-----------------------")
for i in range(1, n + 1):
    print("%d   %d         %d" %(i, i**2, math.factorial(i)))
