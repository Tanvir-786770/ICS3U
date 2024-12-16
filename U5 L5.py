def getInt(prompt):
    i = 0
    while i == 0:
      try:
        ans = int(input(prompt))
        i = 1
        if ans <= 0:
          print("Invalid input. Try again.")
          i = 0
      except:
        print("Invalid input. Try again.")
        i = 0
    return ans

def fib(n):
    if n == 0:
      return 0
    elif n == 1 or n == 2:
      return 1
    else:
      return fib(n-1) + fib(n-2)

# DO NOT ALTER ANY CODE BELOW
tn = getInt("Please input a whole number: ")
for i in range(1, tn + 1):
    print(fib(i), end = " ")
print()
