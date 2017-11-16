# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

jump, i = 0, 0
while i < n-1:
    if (i+2<n) and (c[i+2] == 0):
        i += 2
    else:
        i += 1
    jump += 1

print(jump)

