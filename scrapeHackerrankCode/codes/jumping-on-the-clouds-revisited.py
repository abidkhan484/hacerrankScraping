# Accepted
# Python 3

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
energy, i = 100, 0

while (i+k)%n!=0:

    i = i + k

    if i>n:
        i = i%n

    if c[i]==1:
        energy -= 3
    else:
        energy -= 1

if c[0] == 1:
    energy -= 3
else:
    energy -= 1

print(energy)

