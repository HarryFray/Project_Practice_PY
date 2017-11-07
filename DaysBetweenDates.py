''' To start code assumes no leap year and each month is 30 days long '''

def nextDay(year, month, day):
    newday = day + 1
    if newday > 30:
        newday = 1
        newmonth = month + 1
        newyear = year
        if newmonth > 12:
            newday = 1
            newmonth = 1
            newyear = year + 1
    else:
        newmonth = month
        newyear = year

    return newyear, newmonth, newday

print nextDay(2017, 5, 30)