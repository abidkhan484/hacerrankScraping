# Accepted
# Python 3

#!/bin/python3

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse=True)

miles = 0
for i in range(n):
    miles += (calories[i]<<i)

print(miles)

