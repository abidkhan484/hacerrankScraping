# Terminated due to timeout
# Python 3

#!/bin/python3

import sys

def check_bitwise(n,k):

    mylist = []
    li = [i+1 for i in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            tmp = li[i] & li[j]
            if tmp < k:
                mylist.append(tmp)

    print(max(mylist))
            

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    check_bitwise(n,k)

