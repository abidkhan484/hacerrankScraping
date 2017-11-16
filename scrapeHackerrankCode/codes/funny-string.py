# Accepted
# Python 3

#!/bin/python3
import sys

n = int(input().strip())

for i in range(n):
    s = input().strip()

    l = len(s)
    
    for j in range(l//2):
        temp = abs(ord(s[j]) - ord(s[j+1]))
        tmp = abs(ord(s[l-j-1]) - ord(s[l-j-2]))

        if temp != tmp:
            break

    if temp == tmp:
        print("Funny")
    else:
        print("Not Funny")

