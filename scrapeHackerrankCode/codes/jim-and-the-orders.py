# Accepted
# Python 3

# this problem is still unsolved

n = int(input().strip())
li = []

for _ in range(n):
    p, r = map(int, input().split())
    li.append(p+r)

sort = sorted(li)
for i in range(n):
    for j in range(n):
        if sort[i]==li[j]:
            print(j+1, end=' ')
            li[j] = -1
            break


