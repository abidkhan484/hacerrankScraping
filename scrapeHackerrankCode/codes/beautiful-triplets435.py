# Terminated due to timeout
# Python 3

#!/bin/python3

import sys

n, differ = input().split()
n, differ = int(n), int(differ)

ara = [int(i) for i in input().split()]

count = 0
for i in range(n):
    j = i + 1
    p = ara[i]
    while j < n:
        if p+differ == ara[j]:
            p += differ
            if p == ara[i] + differ*2:
                count += 1
        j += 1
        
print(count)

