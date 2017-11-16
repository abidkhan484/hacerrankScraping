# Runtime Error
# Python 3

#!/bin/python3

import sys

def lcd(a):
    a.sort()
    l = len(a)
    for i in range(1, l):
        a[i] = (a[i]*a[i-1])//gcd([a[i], a[i-1]])

    return a[i]



def gcd(a):
    l = len(a)
    a.sort()
    for i in range(1, l):
        
        while a[i-1] != 0:
            mod = a[i-1]
            temp = a[i-1]            
            a[i-1] = a[i] % a[i-1]
            a[i] = temp

        a[i] = mod
    return a[i]

def getTotalX(a, b):
    count = 0
    p = lcd(a)
    r = gcd(b)
    temp = p
    while (temp>=p) and (temp<=r):
        count += 1
        temp *= 2

    return count

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)

