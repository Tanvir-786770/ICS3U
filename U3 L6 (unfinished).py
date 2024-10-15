import math as m

def factorize(N):
  y = []
  x = m.floor(m.sqrt(N))
  for j in range(1, x + 1):
    if (N % j == 0):
      y.append(j)
  b = y
  for i in b:
    if (N % i == 0 and i >= 2):
      y.append(N / i)
  if (y == []):
    return "This number has no proper factors."
  else:
    return y
      

def sum(a):
  s = 0
  for g in a:
    s += g
  return s


# test values to test your program
print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))

x = 1
while x == 1:
  num = int(input("Enter a number: "))
  h = factorize(num)
  print(h)
  f = sum(h)
  print(f)
