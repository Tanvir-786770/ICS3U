print("--8<--" * 10)

S = "#"
for i in range(11, 0, -1):
  print(S * i)
  
print("\n")

space = " "
s = 5
for h in range(1, 12, 2):
  print(space * s, S * h)
  s -= 1
