# Accepted
# Python 3

#!/bin/python3

import sys

def leap_year(year):
    if (year<1919):
        if (year%4)==0:
            return True
        else:
            return False
    if (year%4)==0:
        if (year%400)==0:
            return True
        elif (year%100)==0:
            return False
        else:
            return True
    else:
        return False

def solve(year):
    # Complete this function
    if year==1918:
        return '26.09.1918'
    elif leap_year(year) is True:
        return '12.09.%s' %year
    elif leap_year(year) is False:
        return '13.09.%s' %year

year = int(input().strip())
result = solve(year)
print(result)

