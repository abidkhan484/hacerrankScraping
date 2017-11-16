# Accepted
# Python 3

#!/bin/python3

n = int(input().strip())
x = [int(temp) for temp in input().split()]
w = list(map(int, input().split()))

su = 0
for i in range(n):
    su += x[i]*w[i]

print("%.1f"%(su/sum(w)))

