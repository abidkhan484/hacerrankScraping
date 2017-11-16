# Accepted
# Python 3

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pr = n
    li = []
    
    while(n):
        i = n%10
        li.append(i)
        n //= 10

    c = 0
    for i in li:
        if (i==0):
            continue
        else:
            if ((pr%i)==0):
                c += 1

    print(c)

