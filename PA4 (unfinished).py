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
    
    return int("%s%s%s" %(r, q, p))


filename = "words40.dat"
fh = open(filename, 'r')

for r in range(1038)
    line = fh.readline()
    line = line.strip()
    m, d, y, word = line.split()
