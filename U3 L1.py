progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
count = 0
for i in progname:
  if i == " ":
    count += 1
    
print("There are", count, "spaces in this text.")
