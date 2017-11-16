# Accepted
# Python 3

n, m = [int(x) for x in input().split()]
summation = 0

for _ in range(m):
    a, b, k = [int(x) for x in input().split()]
    summation += ((b-a+1)*k)

print(summation//n)

