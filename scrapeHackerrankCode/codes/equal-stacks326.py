# Wrong Answer
# Python 3

#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1.reverse(); h2.reverse(); h3.reverse()

a = sum(h1); b = sum(h2); c = sum(h3)
mini = min(a, b, c)

while h1 and h2 and h3:
    mini = min(a, b, c)
    if (a==b) and (a==c):
        break
    if a > mini:
        tmp = h1.pop()
        a -= tmp
    if b > mini:
        tmp = h2.pop()
        b -= tmp
    if c > mini:
        tmp = h3.pop()
        c -= tmp


print(a)

