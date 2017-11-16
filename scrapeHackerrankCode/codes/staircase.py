# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
j = 1

for i in range(n, 0, -1):
    print((i-1)*' '+j*'#')
    j += 1

