def comp(S):
    new = ''
    for x in S:
        if x == "A":
            new = new + ("T")
        elif x == "C":
            new = new + ("G")
        elif x == "G":
            new = new + ("C")
        elif x == "T":
            new = new + ("A")
    return new
S = input("Enter strand: ")

Complement = comp(S)

print("Complementary strand is:", Complement)
