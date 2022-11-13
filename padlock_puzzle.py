def checknum(number, checknumber, num_correct, num_correct_position):
    lnumber = str(number).zfill(len(checknumber))
    return num_correct == sum(lnumber[i] in checknumber for i in range(len(checknumber))) and \
        num_correct_position == sum(lnumber[i] == checknumber[i] for i in range(len(checknumber)))


for cnumber in range(1000):
    if checknum(cnumber, "682", 1, 1) and \
            checknum(cnumber, "614", 1, 0) and \
            checknum(cnumber, "206", 2, 0) and \
            checknum(cnumber, "738", 0, 0) and \
            checknum(cnumber, "780", 1, 0):
        print("Code is:" + str(cnumber).zfill(3))
