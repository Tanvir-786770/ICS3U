def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(wordarr, datearr):
    for i in range(0, len(wordarr) - 1):
        for j in range(i+1, len(wordarr) - 1):
            if (wordarr[i] > wordarr[j]):
                swap(wordarr, i, j)
                swap(datearr, i, j)

def merge(p, q, r):
    if q == "Jan":
        q = "01"
    elif q == "Feb":
        q = "02"
    elif q == "Mar":
        q = "03"
    elif q == "Apr":
        q = "04"
    elif q == "May":
        q = "05"
    elif q == "Jun":
        q = "06"
    elif q == "Jul":
        q = "07"
    elif q == "Aug":
        q = "08"
    elif q == "Sep":
        q = "09"
    elif q == "Oct":
        q = "10"
    elif q == "Nov":
        q = "11"
    elif q == "Dec":
        q = "12"
        
    return int(r+q+p)

def isMatch(array, low, high, item):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == item:
            if array == wordarray:
                return datearray[mid]
            else:
                return wordarray[mid]
        elif array[mid] > item:
            return isMatch(array, low, mid - 1, item)
        else:
            return isMatch(array, mid + 1, high, item)
    else:
        return 0


filename = "wordle.dat"
fh = open(filename, 'r')

wordarray = []
datearray = []

for r in range(1038):
    line = fh.readline()
    line = line.strip()
    m, d, y, word = line.split()
    date = merge(d, m, y)
    wordarray.append(word)
    datearray.append(date)

sort(wordarray, datearray)

print("Welcome to the Wordle Database!")

w = 0
while w == 0:
    searchtype = input("\nEnter 'w' to look for a word, or 'd' to look find the word for a date: ")
    searchtype = searchtype.lower()

    if searchtype == 'w' or searchtype == 'd':
        w = 1
    else:
        print("Invalid input; try again.")


if searchtype == "w":
    word = input("Enter the word you are looking for: ")
    word = word.upper()
    result = isMatch(wordarray, 0, len(wordarray)-1, word)
    if result == 0:
        print(word, "was not found in this database.")
    else:
        print("The word '%s' was the solution to the puzzle on %d." %(word, result))
    

else:
    p = 1
    while p == 1:
        y = 0
        while y == 0:
            try:
                year = int(input("Enter the year: "))
                y = 1
            except:
                print("Invalid input; try again.")
                y = 0
        
        year = str(year)
        m = 0
        while m == 0:
            month = input("Enter the month (3-letter abbreviation; ex: 'Jan'): ")
            if month == 'Jan' or month == 'Feb' or month == 'Mar' or month == 'Apr':
                m = 1
            elif month == 'May' or month == 'Jun' or month == 'Jul' or month == 'Aug':
                m = 1
            elif month == 'Sep' or month == 'Oct' or month == 'Nov' or month == 'Dec':
                m = 1
            else:
                print("Invalid input; try again.")
        d = 0
        while d == 0:
            try:
                day = int(input("Enter the day: "))
                if day >= 1 and day <= 31:
                    d = 1
                else:
                    print("Invalid input; try again.")
            except:
                print("Invalid input; try again.")

        day = str(day)
        if int(day) < 10:
            day = "0" + day
        date = merge(day, month, year)
        if date < 20210619:
            print("No wordles occurred before 20210619. Enter a later date.")
        elif date > 20240421:
            print("The latest wordle on this database is on 20240421. Enter an earlier date.")
        else:
            for s in range(0, len(datearray)-1):
                if datearray[s] == date:
                    print("The solution for the puzzle on", date, "is %s." %wordarray[s])
            p = 0
