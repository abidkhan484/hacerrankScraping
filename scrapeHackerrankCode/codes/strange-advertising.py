# Accepted
# Python 3

#!/usr/bin/env python3

import sys

days = int(input().strip())

ad = 5; summation = 0
temp = ad//2
ad = temp
summation += temp
for i in range(1, days):
    ad *= 3
    temp = ad//2
    ad = temp
    summation += temp
print(summation)

