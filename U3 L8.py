def validate(S):
  invalid = 0
  for x in S:
    if x == "G":
      pass
    elif x == "C":
      pass
    elif x == "T":
      pass
    elif x == "A":
      pass
    else:
      invalid = 1
  if invalid == 1:
    return "Invalid"
  else:
    return "Valid"

a = 1
while a == 1:
  S = input("Enter stray: ")
  h = validate(S)
  if h == "Valid":
    print("Valid!")
  else:
    print("Invalid.")
    pos = 1
    for x in S:
      if x == "G":
        pass
      elif x == "C":
        pass
      elif x == "T":
        pass
      elif x == "A":
        pass
      else:
        print(x, "found in position", pos)
      pos += 1
