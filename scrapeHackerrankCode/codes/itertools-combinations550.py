# Wrong Answer
# Python 3

from itertools import combinations

a, d = input().split()
d = int(d)

res = list(a)
res.sort()
a = ''.join(res)
l = list(combinations(a, d))
le = len(l)
l.sort()

for i in res:
    print (i)

for i in range(le):
    for j in range(d):
        print(l[i][j], end='')
    print()

