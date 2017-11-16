# Wrong Answer
# Python 3

#!/bin/python3

import sys

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)
#  Print the minimum cost of converting 's' into a magic square

li=[]
for i in range(3):
    summation = 0
    for j in range(3):
        summation += s[i][j]
    li.append(summation)

if (li[0]==li[1]):
    print(abs(li[0]-li[2]))
elif (li[1]==li[2]):
    print(abs(li[1]-li[0]))
else:
    print(abs(li[0]-li[1]))
