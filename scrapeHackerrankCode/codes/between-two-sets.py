# Accepted
# Python 3

#!/bin/python3

import sys

def lcd(p):
    a = []
    a.extend(p)
    l = len(a)
    if l==1:
        return a[0]
    a.sort()
    for i in range(l-1):
        a[i] = (a[i+1]*a[i])//gcd([a[i+1], a[i]])

    return a[i]



def gcd(p):
    a= []
    a.extend(p)
    l = len(a)
    if l == 1:
        return a[0]
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
    for i in range(p, r+1, p):
        if (i%p==0) and (r%i==0):
            count += 1

    return count


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)

