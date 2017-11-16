# Wrong Answer
# Python 3

#!/bin/python3
import sys

n, k, q = input().split()
n, k, q = int(n), int(k), int(q)
temp_li = [int(temp) for temp in input().split()]

if n==k:
    li = list(temp_li)
else:
    li = list(temp_li[k-1:])
    li.extend(temp_li[:k-1])


for i in range(q):
    m = int(input().strip())
    print(li[m])


