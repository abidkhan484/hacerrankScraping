# Accepted
# Python 3

#!/bin/python3

import sys


n = int(input().strip())
result = 1
for i in range(1, n+1):
    result *= i

print(result)

