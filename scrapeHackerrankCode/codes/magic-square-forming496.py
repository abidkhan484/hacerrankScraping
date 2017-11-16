# Wrong Answer
# Python 3

#!/bin/python3

import sys

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)
#  Print the minimum cost of converting 's' into a magic square

for i in range(3):
    summation = 0
    for j in range(3):
        summation += s[i][j]
    if summation is not 15:
        break
print(15-summation)

