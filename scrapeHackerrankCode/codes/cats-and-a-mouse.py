# Accepted
# Python 3

#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    #position of cat A to mouse is c1
    c1 = x-z
    if (c1<0):
        c1 = -c1

    #position of cat B to mouse is c2
    c2 = y-z
    if (c2<0):
        c2 = -c2

    if (c1>c2):
        print("Cat B")
    elif (c2>c1):
        print("Cat A")
    else:
        print("Mouse C")

