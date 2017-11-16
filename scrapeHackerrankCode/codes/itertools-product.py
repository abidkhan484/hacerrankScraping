# Accepted
# Python 3

from itertools import product

a=map(int, input().split())
b=map(int, input().split())

cartesian=list(product(a, b))

for i in cartesian:
    print(i, end=' ')

