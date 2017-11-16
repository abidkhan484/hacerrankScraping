# Wrong Answer
# Python 3

#!/bin/python3
import sys

n, k, q = input().split()
n, k, q = int(n), int(k), int(q)
temp_li = [int(temp) for temp in input().split()]

n -= k
li = list(temp_li[n:])
li.extend(temp_li[:n])


for i in range(q):
    m = int(input().strip())
    print(li[m])

