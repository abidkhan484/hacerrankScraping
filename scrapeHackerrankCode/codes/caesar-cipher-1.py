# Accepted
# Python 3

#!/bin/usr/python3

import sys

n = int(input().strip())
st = input()
k = int(input().strip())

# make the input string as a list
st = list(st)
l = len(st)

# loop to encode the string
for i in range(l):

    # this logic do actually the requirement of increasing k amount of string
    if st[i]>='a' and st[i]<='z':
        tmp = ord(st[i])
        tmp += k
        if tmp > 122:
            tmp -= 97
            tmp = tmp%26
            tmp += 97
        st[i] = chr(tmp)

    if st[i]>='A' and st[i]<='Z':
        tmp = ord(st[i])
        tmp += k
        if tmp > 90:
            tmp -= 65
            tmp = tmp%26
            tmp += 65
        st[i] = chr(tmp)

# simply join and print the output
print(''.join(st))

