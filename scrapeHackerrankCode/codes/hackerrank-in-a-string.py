# Accepted
# Python 3

#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    pagli = 'hackerrank'
    while pagli and s:
        if pagli[0]==s[0]:
            pagli = pagli[1:]
            s = s[1:]
        else:
            s = s[1:]

    if pagli:
        print('NO')
    else:
        print('YES')

