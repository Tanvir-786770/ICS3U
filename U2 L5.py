import math

n = int(input("Give me a value of n: "))
print("Counting from j = 1 to %d:\n" %n)
print("j   tri       factorial")
print("-----------------------")
for i in range(1, n + 1):
    print("%d   %d         %d" %(i, i**2, math.factorial(i)))
