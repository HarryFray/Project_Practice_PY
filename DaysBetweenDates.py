''' To start code assumes no leap year and each month is 30 days long '''


''' givin a date adds one day to that date '''
def nextDay(year, month, day):
    if day < 30:
        return year,month,day + 1
    else:
        if month == 12:
            return year + 1,1,1
        else:
            return year,month + 1,1

''' givin two dates returns true if first date occures before second '''
def DateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
       if month1 < month2:
           return True
       elif month1 == month2:
           if day1 < day2:
                return True
    return False


''' givin two dates returns days between them '''
def DaysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while DateIsBefore(year1, month1, day1, year2, month2, day2):
        year1,month1,day1 = nextDay(year1, month1, day1)
        days += days
    return days

print DaysBetweenDates(1991,5,30,2017,11,7)



