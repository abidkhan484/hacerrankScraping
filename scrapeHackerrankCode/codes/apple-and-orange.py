# Accepted
# Python 3

#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

count = 0
for i in range(m):
    temp = a + apple[i]
    if (temp >= s) and (temp <= t):
        count += 1

print(count)

count = 0
for i in range(n):
    temp = b + orange[i]
    if (temp >= s) and (temp <= t):
        count += 1

print(count)

