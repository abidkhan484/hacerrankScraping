# Accepted
# Python 3

import sys

from collections import defaultdict

n, m = input().split()
n, m = int(n), int(m)

d = defaultdict(list)

for i in range(n):
    x = input().strip()
    d[x].append(str(i+1))

k = list(d.keys())

for i in range(m):
    x = input().strip()
    for j in k:
        if (j==x):
            temp_li = list(d[x])
            print(' '.join(temp_li))
            break
    else:
        print(-1)

