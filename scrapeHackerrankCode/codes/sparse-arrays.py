# Accepted
# Python 3

#! /bin/python3

import sys

n = int(input().strip())
li = []
for i in range(n):
    temp = input().strip()
    li.append(temp)

m = int(input().strip())

for i in range(m):
    temp = input().strip()
    c = 0
    for j in range(n):
        if temp == li[j]:
            c += 1
    print(c)

