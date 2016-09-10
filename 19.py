#how many days between 1 Jan 1901 and 31 Dec 2000
dayList = [31,28,31,30,31,30,31,31,30,31,30,31]
monthCounter = 0
yearCounter = 1901
dayCounter = 1
sundayCounter = 0

def countSunday(dayCounter, monthCounter, yearCounter, sundayCounter):
    dayList = [31,28,31,30,31,30,31,31,30,31,30,31]
    if yearCounter % 100 == 0:
        if yearCounter % 400 == 0:
            dayList[1] = 29
    elif yearCounter % 4 == 0:
        dayList[1] = 29
        
    for x in range(0,dayList[monthCounter % 12]):
        if x == 0 and dayCounter % 7 == 6:
            sundayCounter += 1
        dayCounter += 1

    if monthCounter % 12 == 11:
        yearCounter += 1

    monthCounter += 1

    

    return [dayCounter,monthCounter,yearCounter,sundayCounter]


while not(yearCounter == 2000 and monthCounter % 12 == 11):
    L = countSunday(dayCounter,monthCounter,yearCounter,sundayCounter)
    dayCounter = L[0]
    monthCounter = L[1]
    yearCounter = L[2]
    sundayCounter = L[3]


   


