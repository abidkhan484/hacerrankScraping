# Terminated due to timeout
# Python 3

#! /bin/python3
import sys

n, m = input().split()
n, m = int(n), int(m)

li = n * [0]
for i in range(m):
    a, b, k = input().split()
    a, b, k = int(a), int(b), int(k)

    for j in range(a, b+1):
        li[j-1] += k

print(max(li))

