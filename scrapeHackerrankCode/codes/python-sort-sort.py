# Accepted
# Python 3

n, m = input().split()
n, m = int(n), int(m)

li = []
for i in range(n):
    temp = list(map(int, input().split()))
    li.append(temp)

k = int(input().strip())
temp = []
for i in range(n):
    temp.append(li[i][k])

temp.sort()
for i in range(n):
    for j in range(n):
        if temp[i]==li[j][k]:
            for p in range(m):
                print(li[j][p], end=' ')
                li[j][p] = -1
            break
    print()

