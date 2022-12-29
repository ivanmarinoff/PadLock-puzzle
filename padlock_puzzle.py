def padlock(number, checknumber, num_correct, num_correct_position):
    number = str(number).zfill(len(checknumber))
    return num_correct == sum(number[i] in checknumber for i in range(len(checknumber))) and \
        num_correct_position == sum(number[i] == checknumber[i] for i in range(len(checknumber)))


for current_number in range(1000):
    if padlock(current_number, "682", 1, 1) and \
            padlock(current_number, "614", 1, 0) and \
            padlock(current_number, "206", 2, 0) and \
            padlock(current_number, "738", 0, 0) and \
            padlock(current_number, "780", 1, 0):
        print("Code is:" + str(current_number).zfill(3))
'''
One of the numbers is correct and positioned in the correct place - 682. 
Nothing is right - 614. 
One of the numbers is correct but positioned in the wrong place - 206. 
Two of the numbers are correct but positioned in the wrong places - 738. 
One of the numbers is correct but misplaced - 780. 
'''
