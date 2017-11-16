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
temp_li = [int(c) for c in input().split()]
occerence = list(map(int, input().split()))

li = []
for i in range(n):
    li.extend(occerence[i]*[temp_li[i]])

li.sort()

l = len(li)
if l & 1:
    # prints (right_quartiles - left_quartiles)
    print("%.1f" %(median(li[(l//2)+1:]) - median(li[:l//2])))

else:
    # prints (right_quartiles - left_quartiles)
    print("%.1f" %(median(li[(l//2):]) - median(li[:l//2])))

