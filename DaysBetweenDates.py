''' To start code assumes no leap year and each month is 30 days long '''

def nextDay(year, month, day):
    if day < 30:
        return year,month,day + 1
    else:
        if month == 12:
            return year + 1,1,1
        else:
            return year,month + 1,1

print nextDay(2017, 12, 30)