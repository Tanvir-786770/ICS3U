def validate(N):
    arr = []
    num = 0
    for i in range(0, len(N)):
        arr.append(int(N[i]))
    for d in range(len(arr)-2, 0, -2):
        arr[d] *= 2
        if arr[d] >= 10:
            arr[d] -= 9
        num += arr[d]
    for c in range(0, len(arr), 2):
        num += arr[c]

    if num % 10 == 0:
        return True
    else:
        return False

print("Validate a number with thr Luhn Algorithm!")
num = input("Input a number to validate: ")
isValid = validate(num)
if isValid:
    print(num, "is valid! :)")
else:
    print(num, "is not valid! :(")
