# Accepted
# Python 3

#!/bin/python3

def getMinimumCost(n, k, c):

    c.sort(); total = 0; pr = 1
    i = 0; n -= 1
    while i <= n:

        j = k
        while i <= n:
            if not j:
                break
            total += (pr*c[n])
            j -= 1
            n -= 1
        pr += 1

    return total

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)

