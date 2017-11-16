# Wrong Answer
# Python 3

#!/bin/python3

n, k, q = input().split()
n, k, q = int(n), int(k), int(q)
temp_li = [int(temp) for temp in input().split()]

li = list(temp_li[k-1:])
li.extend(temp_li[:k-1])

for i in range(q):
    m = int(input().strip())
    print(li[m])

