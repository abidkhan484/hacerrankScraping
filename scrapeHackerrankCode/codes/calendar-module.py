# Accepted
# Python 3

import calendar

month, day, year = list(map(int, input().split()))

print(calendar.day_name[calendar.weekday(year, month, day)].upper())

