# Accepted
# Python 3

from itertools import combinations_with_replacement

a, d = input().split()

d= int(d)
a=list(a)
a.sort()

li= list(combinations_with_replacement(a, d))
le  = len(li)

for i in range(le):
    for j in range(d):
        print(li[i][j], end='')
    print()
    

