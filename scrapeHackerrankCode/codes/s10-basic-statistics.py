# Accepted
# Python 3

#!/bin/python3

import sys

def mean(li):
    total = sum(li)
    l = len(li)
    return total/l

def median(li):
    l = len(li)
    li.sort()
    if (l//2) != (l/2):
        return li[l//2]
    else:
        total = li[l//2] + li[(l//2)-1]
        return total/2

def mode(li):
    l = len(li)
    li.sort()
    temp = []; res = 1
    num = []; maxim = -1
    
    for i in range(l-1):
        if li[i] != li[i+1]:
            num.append(li[i])
            temp.append(res)
            if maxim < res:
                maxim = res
            res = 1
        else:
            res += 1

    num.append(li[i+1])
    temp.append(res)
    l = len(temp)
    for i in range(l):
        if maxim == temp[i]:
            break
    
    return num[i]

n = int(input().strip())
li = list(map(int, input().split()))
print("%.1f" %mean(li))
print("%.1f" %median(li))
print(mode(li))

