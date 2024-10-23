# Code for Pythagorean Triples
for i in range(1, 101):
    for j in range(i, 101):
      for k in range(1, 101):
         left = i**2 + j**2
         right = k**2
         if left == right:
            print((i, j, k))
            
def pytriples(n):
  if n % 2 != 0 and n >= 3:
    a = n**2
    b = (n / 2) * (n + 1)
    c = (n / 2) * (n + 1) + 1
    return [a, b, c]
  elif n % 2 == 0 and n >= 3:
    m = n**2 / 4
    a = n
    b = m - 1
    c = m + 1
    return [a, b, c]
      
max = int(input("Input the number of pythagorean triples you want: "))
for n in range(3, max+1):
  print(pytriples(n))

