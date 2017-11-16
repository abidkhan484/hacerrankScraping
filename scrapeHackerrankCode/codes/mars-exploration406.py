# Wrong Answer
# Python 3

#!/bin/python3

import sys

s = input().strip()

i, count = 0, 0
while s:
    if (s[i]=='S') and (s[i+1]=='O') and (s[i+2]=='S'):
        s = s[3:]
    else:
        count += 1
        s = s[3:]

print(count)

