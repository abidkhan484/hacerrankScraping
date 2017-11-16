# Accepted
# Python 3

#!/bin/python3

import sys

def solve():
    
    m, n, x = map(int, input().split())
    ar1 = list(map(int, input().split()))
    ar2 = [int(p) for p in input().split()]

    ar1.reverse(); ar2.reverse()
            
    res = 0; count = 0
    for i in range(m-1, -1, -1):
        res += ar1[i]
        count += 1
        if res > x:
            res -= ar1[i]
            count -= 1
            break
    else:
        i = -1

    j = n-1; maxim=count
    while j >= 0:
        res += ar2[j]
        if res > x:
            i += 1
            if i==m:
                break
            res -= (ar2[j]+ar1[i])
            count -= 1
        else:
            j -= 1
            count += 1
        if count > maxim:
            maxim = count

    print(maxim)

for _ in range(int(input().strip())):
    solve()

'''input:
1
20 35 67
19 9 8 13 1 7 18 0 19 19 10 5 15 19 0 0 16 12 5 10
11 17 1 18 14 12 9 18 14 3 4 13 4 12 6 5 12 16 5 11 16 8 16 3 7 8 3 3 0 1 13 4 10 7 14

output: 6
'''

