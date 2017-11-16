# Terminated due to timeout
# Python 3

#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    while m:
        s += 1
        if s >= n:
            s = s%n
        m -= 1
    return s-1

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

