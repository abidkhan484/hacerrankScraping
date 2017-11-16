# Wrong Answer
# Python 3

node, edge = [int(p) for p in input().split()]

mylist = [[] for _ in range(node-1)]

for _ in range(edge):
    a, b, dis = [int(pr) for pr in input().split()]
    if a > b:
        mylist[b-1].append(dis)
    else:
        mylist[a-1].append(dis)

total = 0
for i in range(node-1):
    total += min(mylist[i])

print(total)

