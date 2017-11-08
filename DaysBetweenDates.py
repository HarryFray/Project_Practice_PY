''' To start code assumes no leap year and each month is 30 days long '''

''' adds one day to original date
input: day,month
output: day,month '''

def DaysMonths(month,day):
    DaysInEachMonth = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,
                       '7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
    assert not day > DaysInEachMonth[str(month)]

    MonthLength = DaysInEachMonth[str(month)]
    if day < MonthLength:
        day += 1
        return month, day
    else:
        month += 1
        day = 1
        return month, day


''' givin a date adds one day to that date accounting for change in year '''
def nextDay(year, month, day):
    month,day = DaysMonths(month,day)
    if month == 13:
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


print DaysBetweenDates(1991,5,28,2017,11,7)




