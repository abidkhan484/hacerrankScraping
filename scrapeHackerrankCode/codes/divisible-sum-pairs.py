# Accepted
# Python 3

#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
# write your code here
c = 0
for i in range(n-1):

    for j in range(i+1, n):
        if ((i<j) & ((a[i] + a[j]) % k == 0)):
            c += 1

print(c)

