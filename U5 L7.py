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
    S.append(1)
    S.append(1)
    for i in range(2, n):
        S.append(S[i-1] + S[i-2])
    return

def f(n):
    if n == 1:
        S.append(1)
    elif n == 2:
        S.append(fib(1))
        S.append(1)
    else:
        fib(n - 1)
        L = len(S)
        S.append(S[L-1] + S[L-2])
        

n = getInt("Please input a whole number greater than 0: ")

S = []

fib(n)

print(S)
print("\nThese are the first %d fibonacci numbers." %len(S))
