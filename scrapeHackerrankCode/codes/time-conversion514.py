# Wrong Answer
# Python 3

#!/bin/python3

import sys


time = input().strip()
temp = time.split(':')

if (temp[2][2]=='A'):
    temp[2] = temp[2][:2]
elif (temp[2][2]=='P'):
    temp[2] = temp[2][:2]
    temp[0] = str(int(temp[0]) + 12)

print(':'.join(temp))

