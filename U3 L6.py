import math as m

def factorize(N):
  y = []
  x = m.floor(m.sqrt(N))
  for j in range(1, x + 1):
    if (N % j == 0):
      if (j != N):
       y.append(j)
  b = []
  for i in y:
    b.append(i)
  for k in b:
    if (k > 1):
      y.append(int(N / k))
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
  num = int(input("Enter a positive integer: "))
  if (num > 0):
    h = factorize(num)
    print(h)
    if (h == "This number has no proper factors."):
      print("%d is a deficient number." %num)
    else:
      print("The sum of the factors is %d." %sum(h))
      if sum(h) == num:
        print("%d is a perfect number." %num)
      elif sum(h) > num:
        print("%d is an abundant number." %num)
      elif sum(h) < num:
        print("%d is a deficient number." %num)
  else:
    print("Invalid input.")
