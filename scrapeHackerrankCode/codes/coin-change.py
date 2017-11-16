# Accepted
# Python 3

# the problem is not solved yet

#!/bin/python3

import sys

def getWays(n, c):

    # i can use (m) var bcoz it is globally decleared
    ar = [[0 for p in range(n+1)] for i in range(m)]
    for i in range(m):
        ar[i][0] = 1
        
    c.sort()
    j = c[0]
    while j < n+1:
        ar[0][j] = 1
        j += c[0]

    for i in range(1, m):
        p = c[i]
        for j in range(1, n+1):
            if (j-p) >= 0:
                ar[i][j] = ar[i-1][j] + ar[i][j-p]
            else:
                ar[i][j] = ar[i-1][j]

    return ar[-1][-1]
        

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)


'''
input:
10 4
2 5 3 6

o:
5

input:
4 3
1 2 3

o:
4
'''

