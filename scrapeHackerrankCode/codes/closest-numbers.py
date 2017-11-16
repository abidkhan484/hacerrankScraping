# Accepted
# Python 3

n = int(input().strip())
li = list(map(int, input().split()))

li.sort()

tmp, minim = [], 10000001
for i in range(1, n):
    #sub variable to check the difference
    sub = li[i] - li[i-1]
    if  sub < minim:
        minim = sub
        tmp = []
        tmp.append(li[i-1])
        tmp.append(li[i])
    elif sub == minim:
        tmp.append(li[i-1])
        tmp.append(li[i])

print(*tmp)

