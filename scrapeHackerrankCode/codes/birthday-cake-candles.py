# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

height.sort()
c=0
high = height[n-1]

for  i in range(n):

    if (height[i] != high):
        c+=1
    else:
        break
        
print(n-c)
