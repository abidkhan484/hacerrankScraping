# Accepted
# Python 3

import math

for _ in range(int(input().strip())):
    p, r = input().split()
    p, r = int(p), int(r)
    a = r-1

    pria = (math.factorial(p+a)//(math.factorial(p)*math.factorial(a)))
    print(pria%(10**9+7))

