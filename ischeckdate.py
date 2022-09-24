T = int(input())



for testcase in range(T):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    iyear = int(year)
    imonth = int(month)
    iday = int(day)
    if (imonth == 1 or imonth == 3 or imonth == 5 or imonth == 7 or imonth == 8 or imonth == 10 or imonth == 12) and imonth !=0 and 0 < iday <= 31:
        print("#{} {}/{}/{}".format(testcase+1, year, month, day))
    elif imonth == 2 and imonth !=0 and 0 < iday <= 28:
        print("#{} {}/{}/{}".format(testcase+1, year, month, day))
    elif (imonth == 4 or imonth == 6 or imonth == 9 or imonth == 11) and imonth !=0 and 0 < iday <= 30:
        print("#{} {}/{}/{}".format(testcase+1, year, month, day))
    else:
        print("#{} -1".format(testcase+1))

    