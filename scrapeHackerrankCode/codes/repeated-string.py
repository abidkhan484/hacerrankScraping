# Accepted
# Python 3

#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

l = len(s)
pri = n//l
a = n%l

count, additional = 0, 0
for i in range(l):
    if i<a and s[i]=='a':
        count += 1
        additional += 1
    elif s[i]=='a':
        count += 1

print((count*pri)+additional)

