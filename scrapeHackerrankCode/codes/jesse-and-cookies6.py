# Runtime Error
# Python 3

n, m = map(int, input().split())
ar = [int(p) for p in input().split()]
ar.sort()

c = -1
while ar[0] < m:
    tmp = (ar[0]*1) + (ar[1]*2)
    del ar[0]; del ar[1]
    ar.append(tmp)
    ar.sort()
    c += 1

print(c)

