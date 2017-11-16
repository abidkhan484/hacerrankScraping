# Accepted
# Python 3

from math import sqrt
from math import floor

def factor_generate(n, j=0):
    if n&1:
        return 0

    all_factor = []
    p = floor(sqrt(n)); i = 2
    while i<=p:
        if not n%i:
            if not i&1:
                all_factor.append(i)
            ria = n//i
            if not ria&1:
                all_factor.append(ria)

        i += 1

    all_factor.append(n)
    result = len(set(all_factor))

    return result



for _ in range(int(input().strip())):
    print(factor_generate(int(input().strip())))

