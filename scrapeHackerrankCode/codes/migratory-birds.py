# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
#(var) count is to use know about the birds
count = 5*[0]
#loop to count the birds
for i in types:
    if i == 1:
        count[0] += 1
    elif i == 2:
        count[1] += 1
    elif i == 3:
        count[2] += 1
    elif i == 4:
        count[3] += 1
    elif i == 5:
        count[4] += 1

big = -1
# loop to check the biggest numbers of birds
for i in range(5):
    if count[i] > big:
        big = count[i]
        n = i+1

print(n)

