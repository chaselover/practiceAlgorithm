T = int(input())



for testcase in range(T):
    date = input()
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    if (month == 1 or 3 or 5 or 7 or 8 or 10 or 12) and month !=0 and 0 < day <= 31:
        print("#{} {}/{}/{}".format(testcase+1, year, month, day))
    elif month == 2 and month !=0 and 0 < day <= 28:
        print("#{} {}/{}/{}".format(testcase+1, year, month, day))
    elif (month == 4 or 6 or 9 or 11) and month !=0 and 0 < day <= 30:
        print("#{} {}/{}/{}".format(testcase+1, year, month, day))
    else:
        print("#{} -1")

    