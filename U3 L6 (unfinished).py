import math as m

def factorize(N):
  y = []
  x = m.sqrt(N)
  for j in range(1, m.floor(x)):
    if (N % j == 0):
      y.append(j)
  if (y == []):
    return "This number has no proper factors."
  else:
    return y
      

# test values to test your program
print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))
