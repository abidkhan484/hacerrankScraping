# Wrong Answer
# Python 3

#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    if (((n-p)//2)>(p//2)):
        return p//2
    else:
        return (n-p)//2

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)

