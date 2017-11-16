# Accepted
# Python 3

#!/bin/python3
import sys

# this function return the median of the list
def median(li):
    l = len(li)

    # if you don't understand this logic. then check the role of median
    # here l & 1 returns true if l is odd
    if l & 1:
        return li[l//2]
    else:
        total = li[l//2] + li[(l//2)-1]
        return total/2


n = int(input().strip())
li = list(map(int, input().split()))

li.sort()
l = len(li)

if l & 1:
    print("%d" %median(li[:l//2]))
    print(li[l//2])
    print("%d" %median(li[(l//2)+1:]))

else:
    print("%d" %median(li[:l//2]))
    print("%d" %median(li))
    print("%d" %median(li[(l//2):]))

