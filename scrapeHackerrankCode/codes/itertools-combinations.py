# Accepted
# Python 3

from itertools import combinations

a, d = input().split()
d = int(d); res=[]

a = list(a)
a.sort()
for i in range(d):
    li = list(combinations(a, i+1))
    priya = len(li)
    for j in range(priya):
        lol= len(li[j])
        for k in range(lol):
            print(li[j][k], end= '')
        print()

