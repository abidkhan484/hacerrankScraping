# Accepted
# Python 3

#!/bin/python3

import sys

n = int(input().strip())

for i in range(n):
    p = int(input().strip())
    i = p//2
    if p%2==0:
        print(2**(i+1)-1)
    else:
        print((2**(i+2)-1)-1)

