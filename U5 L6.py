def triangle (ch, num):
  # Change this code for the exercise:
  print(ch*num)
  if (num == 1): # base case
    # we’re done
    return
  else: # recursive step
    triangle(ch, num - 1)
  return

# DO NOT ALTER CODE AFTER THIS COMMENT
c = "#"
n = 7
triangle(c, n)
