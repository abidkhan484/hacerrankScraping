# Wrong Answer
# Python 3

from itertools import permutations

a, d = input().split()
a = a.upper()
d = int(d)

l = list(permutations(a, d))
le = len(l)
l.sort()

for i in range(le):
    print(l[i][0]+l[i][1])

