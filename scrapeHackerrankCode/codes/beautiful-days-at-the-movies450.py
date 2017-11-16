# Accepted
# Python 3

#!/bin/python3
import sys

def reverse(x):
    temp = 0
    while x:
        t = x%10
        temp = temp*10 + t
        x = x//10
    return temp

n, m, k = input().split()
n, m, k = int(n), int(m), int(k)
summation = 0

while n<=m:
    temp = reverse(n)
    temp -= n
    if temp<0:
        temp = -temp
    temp = temp/k
    if temp==int(temp):
        summation += 1

    n += 1

    
print(summation)

