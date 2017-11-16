# Accepted
# Python 3

#!/bin/python3

import sys


s = input().strip()
count = 0
for i in s:
    if (i>='A') and (i<='Z'):
        count += 1
        continue

print(count+1)

