# Accepted
# Python 3

from math import sqrt
from math import floor


#the function return all prime factor in a num
def prime_factorization(n):

    total = 0
    ia = sqrt(n); j = 3
    # this while loop make the number odd
    while not (n&1):
        total += 2
        n = n >> 1
    # this loop get another prime number that can devide our main number
    while (n>1) and (j <= ia):
        if not (n%j):
            n = n // j
            total += digit_sum(j)
        else:
            j += 2

    if n>1:
        total += digit_sum(n)
        
    return total

# this function return the sum of all digits
def digit_sum(n, j=0):
    if not n:
        return j
    return digit_sum(n//10, j+(n%10))


num = int(input().strip())
print(1) if prime_factorization(num)==digit_sum(num) else print(0)

