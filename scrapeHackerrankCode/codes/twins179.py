# Wrong Answer
# Python 3

# this problem is still unsolved

import math

# the function returns all the prime numbers in a number
def all_prime_between_a_num(num):

    if num < 2:
        return []
    mylist = [1]*num
    mylist[0] = 0

    for i in range(1, num, 2):
        mylist[i] = 0

    for i in range(3, math.floor(math.sqrt(num))+2, 2):
        if mylist[i-1] == 0:
            continue
        p = i-1+i
        for j in range(p, num, i):
            mylist[j] = 0

    ar = [2]
    for i in range(num):
        if mylist[i]:
            ar.append(i+1)

    return ar


def prime_divisor(num):

    pagli = num//2
    for i in range(3409):
        if not num%ar[i]:
            return False
        if pagli < ar[i]:
            break
    return True

def prime_on_range(start, end):

    for i in range(start, end+1):
        if not (prime_divisor(i)):
            arr[i-start]=0

start, end = map(int, input().split())
arr = [1] * (end-start+1)
ar = all_prime_between_a_num(31700)
prime_on_range(start, end)

count = 0
for i in range(end-start-1):
    if arr[i]:
        if arr[i+2]:
            count += 1

print(count)

