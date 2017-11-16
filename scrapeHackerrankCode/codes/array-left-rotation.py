# Accepted
# Python 3

#! /bin/python3

import sys

m, n = input().split()
m, n = [int(m), int(n)]

li = input().split()
li2 = []
for i in range(n, m):
    li2.append(li[i])

for i in range(n):
    li2.append(li[i])

for i in range(m):
    print(li2[i], end=' ')

