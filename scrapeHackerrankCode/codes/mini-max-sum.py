# Accepted
# Python 3

#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

p = [a, b, c, d, e]
minimum = 100000000001
maximum = -100000000001

for i in range(5):
    j=0
    total = 0
    while (j<5):
        if (j==i):
            j += 1
        else:
            total += p[j]
            j += 1

    if (total<minimum):
        minimum = total
    if (total>maximum):
        maximum = total
    

print(minimum, maximum)

