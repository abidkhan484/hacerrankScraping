# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.sort()
c, i = 1, 1
temp = n

print(n)
while i < n:
    if arr[i]==arr[i-1]:
        c += 1
    else:
        temp = temp-c
        print(temp)
        c = 1
    i += 1

