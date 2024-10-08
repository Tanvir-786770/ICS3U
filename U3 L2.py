n = int(input("How many items are you entering? "))
items = [""] * n
x = 0
while (x < n):
  y = input("Enter next item: ")
  items[x] = y
  x += 1
print("You have entered", len(items), "items.")
x = 0
while (x < n):
  print(items[x])
  x += 1
