# Accepted
# Python 3

#!/bin/python3

import sys


N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

food = 0
for i in range(N-1):
    if B[i] & 1:
        B[i] += 1
        B[i+1] += 1
        food += 2

if B[i+1] & 1:
    print('NO')
else:
    print(food)

