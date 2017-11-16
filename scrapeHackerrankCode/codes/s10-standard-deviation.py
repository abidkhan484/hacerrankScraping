# Accepted
# Python 3

#!/bin/python3

import sys
import math

n = int(input().strip())
li = list(map(int, input().split()))

mean = sum(li)/n
total = 0
for i in range(n):
    total += (li[i]-mean)**2

total = math.sqrt(total/n)
print("%.1f" %total)

