# Accepted
# Python 3

#! /bin/python3
import sys

n = int(input().strip())
li = list(map(int, input().strip().split()))

for i in range(1, n):
    temp = li[i]
    j = i-1
    p = i
    while (j>=0):
        if (temp > li[j]):
            break
        else:
            li[p] = li[j]
            p -= 1
        j -= 1
    li[p] = temp
    for k in li:
        print(k, end=' ')
    print()

