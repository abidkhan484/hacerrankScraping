# Terminated due to timeout
# Python 3

#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if (x1 > x2):
    maximum = x1
    minimum = x2
    max_v = v1
    min_v = v2
else:
    maximum = x2
    minimum = x1
    max_v = v2
    min_v = v1

if ((v2<v1) and (x2<x1)) or ((v2>v1) and (x2>x1)):
    print('NO')
else:
    while True:
        if (maximum == minimum):
            print('YES')
            break
        elif (minimum > maximum):
            print('NO')
            break
        else:
            maximum += max_v
            minimum += min_v

