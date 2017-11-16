# Wrong Answer
# Python 3

#!/bin/python3

import sys


d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

fine = 0
if d1>d2:
    temp = d1-d2
    fine = temp*15
if m1>m2:
    temp = m1-m2
    fine = temp*500
if y1>y2:
    temp = y1-y2
    fine = temp*10000

print(fine)

