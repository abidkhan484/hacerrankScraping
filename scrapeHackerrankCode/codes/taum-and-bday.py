# Accepted
# Python 3

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    p = b*x + w*y
    x_price = b*x + w*x + w*z
    y_price = b*y + w*y + b*z

    print(min(p, x_price, y_price))

