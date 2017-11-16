# Wrong Answer
# Python 3

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i, su = 0, 0
    while i<=n:
        if i==1:
            su += 1
        elif i%2 == 0:
            su += 1
        else:
            su += 3

        i += 1

    print(su)

