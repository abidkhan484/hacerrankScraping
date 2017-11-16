# Accepted
# Python 3

def findHead(idx):
    if par[idx]==idx:
        return idx
    return findHead(par[par[idx]])

def union(a, b):
    u = findHead(a); v = findHead(b)
    if u==v:
        return False

    par[u] = v
    return True

def find_position(num):
    for i in range(edge):
        if mylist[i][-1]==num:
            return i

node, edge = map(int, input().split())

par = [i for i in range(node)]

mylist = []; idx = []
for i in range(edge):
    p = [int(x) for x in input().split()]
    mylist.append(p)
    idx.append(p[-1])

idx.sort(); p = 1; i=0; total=0
while p < node:
    
    position = find_position(idx[i])
    if union((mylist[position][0])-1, (mylist[position][1])-1):
        p += 1
        total += idx[i]
    mylist[position] = [-1]
    i += 1

print(total)

