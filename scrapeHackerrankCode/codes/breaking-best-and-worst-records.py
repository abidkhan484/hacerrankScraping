# Accepted
# Python 3


#!/bin/python3

import sys


n = input()

p = list(map(int, input().split()))

large=p[0]; less=p[0]
c, d = 0, 0
l = len(p)
for i in range(1, l):
    if (p[i] > large):
        large = p[i]
        c += 1
    if (p[i] < less):
        less = p[i]
        d += 1

print(c,d)

