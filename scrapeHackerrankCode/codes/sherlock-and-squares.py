# Wrong Answer
# Python 3

#!/bin/usr/env python3

import sys
import math

n = int(input().strip())

for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)

    a = math.floor(math.sqrt(a))
    b = math.floor(math.sqrt(b))

    if a != b:
        print(b-a)
    else:
        print(0)

