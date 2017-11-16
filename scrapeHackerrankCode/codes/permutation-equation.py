# Accepted
# Python 3

#!/bin/python3

import sys

n = int(input().strip())
a = [int(test) for test in input().split()]

x = 1
p = 0
while p < n:
    for i in range(n):
        if a[i]==x:
            temp = i+1
            for j in range(n):
                if temp==a[j]:
                    print(j+1)
            x += 1
    p += 1

