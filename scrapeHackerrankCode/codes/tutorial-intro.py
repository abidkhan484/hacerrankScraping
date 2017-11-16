# Accepted
# Python 3

V = int(input().strip())

n = int(input().strip())
ar = list(map(int, input().split()))

for i in range(n):
    if (ar[i] == V):
        print(i)
    if (ar[i] > V):
        break

