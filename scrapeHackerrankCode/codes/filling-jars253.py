# Terminated due to timeout
# Python 3

n, m = [int(x) for x in input().split()]
mylist = [0 for _ in range(n)]

for _ in range(m):
    a, b, k = [int(x) for x in input().split()]
    for i in range(a-1, b):
        mylist[i] += k

print(sum(mylist)//n)

