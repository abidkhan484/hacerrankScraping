# Accepted
# Python 3

from math import sqrt
from math import floor

#n = int(input().strip())

def prime_generate(num):
    mylist = [1]*num
    mylist[0] = 0

    for i in range(1, num, 2):
        mylist[i] = 0

    for i in range(3, floor(sqrt(num))+2, 2):
        if mylist[i-1] == 0:
            continue
        p = i-1+i
        for j in range(p, num, i):
            mylist[j] = 0

        #print(mylist)

#    print(mylist)
    li = [2]
    for i in range(num):
        if mylist[i]:
            li.append(i+1)

    del mylist

    return li

li = prime_generate(100)


for _ in range(int(input().strip())):
    n = int(input().strip())
    i = 0
    total = 1
    while total <= n:
        total *= li[i]
        i += 1
    print(i-1)

