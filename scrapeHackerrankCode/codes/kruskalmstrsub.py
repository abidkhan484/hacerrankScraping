# Accepted
# Python 3

def find(idx):
    if par[idx]==idx:
        return idx
    return find(par[idx])

def union(a, b):
    u=find(a); v=find(b)
    if u==v:
        return False
    par[v]=u
    return True



node, edge = map(int, input().split())
arr = []
arr.append(list(map(int, input().split())))
for i in range(edge-1):
    a, b, c = map(int, input().split())
    if c > arr[-1][-1]:
        arr.append([a,b,c])
        continue
    for j in range(len(arr)-1, -1, -1):
        if c > arr[j][-1]:
            arr.insert(j+1, [a,b,c])
            break
    else:
        arr.insert(0, [a,b,c])

#r = int(input().strip())

par = [i for i in range(node)]

total = 0
for i in range(len(arr)):
    if union(arr[i][0]-1, arr[i][1]-1):
        total += arr[i][2]

print(total)

'''
while True:
    findList(pos)
    pllist.append(pos)
    np=checkUnion()

    if not np:
        break

    if np[0] not in pllist:
        pos = np[0]
    else:
        pos=np[1]

    total += np[2]

print(total)



5 7
1 2 20
1 3 50
1 4 70
1 5 90
2 3 30
3 4 40
4 5 60
2

150

4 6
2 1 1000
3 4 299
2 4 200
2 4 100
3 2 300
3 2 6
2

1106

5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1

15
'''

