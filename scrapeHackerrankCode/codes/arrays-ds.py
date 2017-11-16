# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.reverse()

for i in arr:
    print(i, end=' ')

