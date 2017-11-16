# Accepted
# Python 3

#!/bin/python3

import sys


time = input().strip()
temp = time.split(':')

if (temp[2][2]=='A'):
    if (temp[0]=='12'):
        temp[2] = temp[2][:2]
        temp[0] = '00'
    else:
        temp[2] = temp[2][:2]
elif (temp[2][2]=='P'):
    if (temp[0]=='12'):
        temp[2] = temp[2][:2]
    else:
        temp[2] = temp[2][:2]
        temp[0] = str(int(temp[0]) + 12)

print(':'.join(temp))

