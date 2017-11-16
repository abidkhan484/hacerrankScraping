# Accepted
# Python 3

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count = 0
for p in range(n):
    j = 1
    i = 0
    while(j<n):
        if (a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            #print(a)
            count += 1
        i += 1
        j += 1

print("Array is sorted in %d swaps." %count)
print("First Element: %d\nLast Element: %d" %(a[0], a[n-1]))

