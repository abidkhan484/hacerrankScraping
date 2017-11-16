# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

minim = 100001

# loop to check the whole array
for i in range(n):
    j = i + 1
    # this loop check if the number is on the list
    while j < n:
        if A[i]==A[j]:
            break
        j += 1

    # now this j is the distance of the numbers
    if j != n:
        j -= i

    # this statement of the code checks the minimum which will be the output
    if j != n and j < minim:
        minim = j

if minim != 100001:
    print(minim)
else:
    print(-1)

