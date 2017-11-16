# Accepted
# Python 3

from collections import OrderedDict

n = int(input().strip())
dic = OrderedDict()

for i in range(n):
    t = input().split()
    p = ' '.join(t[:-1])
    r = t[-1]
    if p in dic:
        dic[p] += int(r)
    else:
        dic[p] = int(r)

for i in dic:
    print(i, dic[i], end=' ')
    print()

