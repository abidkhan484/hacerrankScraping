# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
count = 0

for i in range(n):
    j = i+1
    while(j < n) and (c[i] != -1):
        if (c[i]==c[j]):
            c[i] = -1
            c[j] = -1
            count += 1
            break
        j += 1
        
print(count)

