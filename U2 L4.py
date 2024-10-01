x = 1
count = 0
n = int(input("Enter a value for the upper limit: "))
while (count <= n):
  print("%d! is %d" %(count,x))
  count += 1
  x *= count
