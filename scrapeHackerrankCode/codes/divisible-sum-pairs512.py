# Wrong Answer
# Python 3

#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
# write your code here
c = 0
for i in range(n):

    for j in range(n):
        if ((a[i] < a[j]) & ((a[i] + a[j]) % k == 0)):
            c += 1

print(c)

