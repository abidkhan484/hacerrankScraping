# Runtime Error
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

def findList(pos):

    for i in range(edge):
        if (arr[i][0]==pos) or (arr[i][1]==pos):
            li.append((i, arr[i][2]))
            mylist.append(arr[i][2])

    mylist.sort()        
    
    return li, mylist


def checkNode():
    f = find(par[0])
    for i in range(1,node):
        if f != find(par[i]):
            return False
    return True

def checkUnion():
    for i in range(len(mylist)):
        for j in range(len(li)):
            if mylist[i]==li[j][-1]:
                if union(arr[li[j][0]][0]-1, arr[li[j][0]][1]-1):
                    pos=arr[li[j][0]]
                    arr[li[j][0]]=[-1,-1,100001]
                    li[i] = (-1,100001)
                    mylist[i]=100001
                    return pos
                else:
                    li[i]=(-1,100001)
                    mylist[i]=100001


node, edge = map(int, input().split())
arr = [[int(p) for p in input().split()] for _ in range(edge)]
r = int(input().strip())

par = [i for i in range(node)]
li = []; pos=r; mylist=[]; total=0
pllist = []

while not checkNode():
    findList(pos)
    pllist.append(pos)
    np=checkUnion()
    if np[0] not in pllist:
        pos = np[0]
    else:
        pos=np[1]

    total += np[2]

print(total)

'''
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

