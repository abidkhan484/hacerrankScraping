# Accepted
# Python 3

from math import floor

b, a = input().split()
b, a = int(b), int(a)

h = (2*a)/b
x = floor(h)
if h>x:
    print(x+1)
else:
    print(x)

