# Runtime Error
# Python 3

n, m, k = map(int, input().split())

mylist = [[1 for _ in range(m)] for _ in range(n)]

for i in range(k):
    p, q, r = map(int, input().split())
    for j in range(q-1, r):
        mylist[p-1][j] = 0

total = 0
for i in range(n):
    for j in range(m):
        if mylist[i][j]:
            total += 1

print(total)

