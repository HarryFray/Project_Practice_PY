''' To start code assumes no leap year and each month is 30 days long '''


''' adds Feb 29 for leap years '''
''' Algorithm from wiki '''

def LeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True

''' calls leap year and increments by one day accounting for monthes 
 respective lengths in days'''
def DaysMonths(year,month,day):
    DaysInEachMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap = LeapYear(year)
    if LeapYear(year) : DaysInEachMonth[2-1] = 29
    assert not day > DaysInEachMonth[month-1]
    MonthLength = DaysInEachMonth[month-1]
    if day < MonthLength:
        day += 1
        return year, month, day
    else:
        month += 1
        day = 1
        return year, month, day

''' givin a date calls day months adding incrimenting year if required '''
def nextDay(year, month, day):
    year,month,day = DaysMonths(year,month,day)
    if month > 12:
         return year + 1,1,1
    else:
        return year,month,day


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
    assert (DateIsBefore(year1, month1, day1, year2, month2, day2))
    while DateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

''' used to calculate years '''
yeardays = 365.2422
''' test cases '''
assert DaysBetweenDates(1991,5,30,2017,11,28)
assert DaysMonths(2000,5,31)
assert nextDay(2000,12,31)
assert DateIsBefore(2000,5,5,2001,5,5)
assert not DateIsBefore(2000,5,5,1999,5,5)



