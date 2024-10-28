import math as m

def factors(N):
    facs = [1]
    for i in range(2, m.floor(m.sqrt(N))+1):
        if N % i == 0:
            facs.append(i)
    return facs

print("Welcome to the School Yearbook Efficiency Calculator!")

x = 1
while x == 1:
    y = 1
    while y == 1:
        N = int(input("\nPlease enter the number of photos you have: "))
        if N > 0:
            y = 0
        else:
            print("%d is an invalid number. Please enter a positive number greater than 0." %N)
    factorlist = factors(N)
    E = len(factorlist) - 1
    Dim1 = factorlist[E]
    Dim2 = int(N / Dim1)
    
    print("The smallest possible perimeter is %d, with the dimensions %d by %d" %(Dim1*Dim2,Dim1,Dim2))
    print("")
    for p in range(1, Dim2 + 1):
        print("#" * Dim1)
