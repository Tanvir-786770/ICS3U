ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
  print() # Above code will list the 3 arrays, seperated by spaces and without the brackets.

print(ar2) # The three arrays will be printed in the exact form of the assigned value of ar2.
print("-----")

y = []

for i in range(len(ar2)):
  x = 0
  ar3 = ar2[i]
  for j in range(len(ar3)):
    x += ar3[j]
  y.append(x)
print(y)
