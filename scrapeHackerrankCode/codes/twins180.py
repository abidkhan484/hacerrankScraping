# Runtime Error
# Python 3

# this problem is still unsolved

import math

def prime_divisor(num):

    pagli=int(math.sqrt(num))+1
    mylist=[1]*pagli

    li = []
    for i in range(3, pagli, 2):
        if (not (num%i)) and (mylist[i]):
            li.append(i)
            tmp = i+i
            for p in range(tmp, pagli, i):
                mylist[p] = 0
    return li

def make_prime_sieve(inc, pos):

    for i in range(pos, length, inc):
        arr[i] = 0

def prime_on_range(start, end):

    if start&1:
        make_prime_sieve(2, 1)
        curr=start
    else:
        make_prime_sieve(2, 0) if start>2 else make_prime_sieve(2, 2)
        curr=start+1

    li = []; pos=0
    for i in range(start, end+1, 2):
        if arr[i-start]:
            mylist=prime_divisor(i)
            for p in range(len(mylist)):
                if mylist[p] not in li:
                    make_prime_sieve(mylist[p], i-start)
                    li.append(mylist[p])
    return

start, end = map(int, input().split())
arr = [1] * (end-start+1)
length = end-start+1; count = 0
prime_on_range(start, end+1)
for i in range(length-2):
    if arr[i]:
        if arr[i+2]:
            count += 1

print(count)

