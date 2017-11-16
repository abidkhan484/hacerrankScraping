# Accepted
# Python 3

#!/bin/python3

import sys

s = input().strip()

count = 0
s = list(s)
l = len(s); j = 0

msg = list('SOS')
for i in range(l):
    if s[i] != msg[j]:
        count += 1
    j += 1
    if j == 3:
        j = j%3

print(count)

