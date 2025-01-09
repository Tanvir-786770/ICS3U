filename = "data.dat"

fh = open(filename, "r")

namelist = []
surnamelist = []
cctypelist = []
ccnumberlist = []
expdatelist = []

fh.readline()

for i in range(200):
    line = fh.readline()
    line = line.strip()
    givenname, surname, cctype, ccnumber, expmo, expyr = line.split(",")
    namelist.append(givenname)
    surnamelist.append(surname)
    cctypelist.append(cctype)
    ccnumberlist.append(ccnumber)
    if int(expmo) < 10:
        expmo = "0" + expmo
    expdate = expyr + expmo
    expdatelist.append(int(expdate))