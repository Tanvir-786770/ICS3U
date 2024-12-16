def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def iSort(A):
    for i in range(1, len(A)-1):
        for j in range(0, i - 1):
            if (A[i] < A[j]):
                swap(A, i, j)

def trim(word):
    word = word.replace('\n', '')
    return word

def printIt(A):
    for i in range(4):
        for w in range(0 + (10*i), 10 + (10*i)):
            print(A[w], end=' ')
        print("\n")

filename = 'words40.dat'
wordarray = []

fh = open(filename, "r")

for i in range(40):
    word = fh.readline()
    word = trim(word)
    wordarray.append(word)

fh.close()

iSort(wordarray)

printIt(wordarray)

print("\n%d words." %len(wordarray))

