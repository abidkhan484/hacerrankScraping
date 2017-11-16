# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum1, sum2 = 0, 0
for i in range(n):
    sum1 += a[i][i]

j=n-1
for i in range(n):
    sum2 += a[i][j]
    j -= 1

sum1 = abs(sum1-sum2)

print(sum1)


