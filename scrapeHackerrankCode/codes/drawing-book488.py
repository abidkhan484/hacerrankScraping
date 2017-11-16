# Wrong Answer
# Python 3

#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    if (n-p) is 1:
        if (n%2) is 0:
            return 1
        else:
            return 0
    elif (n-p) is 0:
        return 0
    else:
        if (((n-p)//2)>(p//2)):
            return p//2
        else:
            return (n-p)//2
        
        
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)

