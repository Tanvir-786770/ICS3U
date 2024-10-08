items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): # Predict A: Will count the number of letters in each item, and assign the integers all into one array assigned to sizeI
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)): # Predict B: Will list each item, but before that, will write the number of letters in the name of each item.
    print("%d %s" % (sizes[i], items[i]))
    
for i in range(len(items)):
  if sizes[i] == len(items[i]):
    print("The size for '%s' is valid." %items[i])
