# Runtime Error
# Python 3

from math import sqrt
from math import floor

def prime_on_range(start, end):

    count=0; length = end + 1
    li = [1] * length
    loop = floor(sqrt(length)) + 1

    for i in range(4, length, 2):
        li[i] = 0

    for i in range(3, loop, 2):
        tmp = i
        tmp += i
        while tmp < length:
            li[tmp] = 0
            tmp += i

    li[0] = 0; li[1] = 0
    
    for i in range(start, length-2):
        if li[i] and li[i+2]:
            count += 1

    return count


start, end = map(int, input().split())
print(prime_on_range(start, end))

