# Accepted
# Python 3

#!/bin/python3

import sys

n = int(input().strip())
for i in range(n):
    st = input().strip()
    c = 0
    l = len(st)
    # this loop check, if the characters are same
    for j in range(1, l):
        if st[j]==st[j-1]:
            c += 1

    print(c)

