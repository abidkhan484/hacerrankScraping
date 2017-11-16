# Accepted
# Python 3

def findHead(idx):

    if ar[idx]==idx:
        return idx
    return findHead(ar[idx])

def union(a, b):

    u = findHead(a); v = findHead(b)
    if u==v:
        return
    ar[u] = v

def checkConnection(i, j):

    li = []
    if (((i-1)>=0) and ((j-1)>=0)) and arr[i-1][j-1]:
        li.append((i-1, j-1))
    if ((j-1)>=0) and arr[i][j-1]:
        li.append((i, j-1))
    if (((i+1)<row) and ((j-1)>=0)) and arr[i+1][j-1]:
        li.append((i+1, j-1))
    if (i-1)>=0 and arr[i-1][j]:
        li.append((i-1, j))
    if (i+1)<row and arr[i+1][j]:
        li.append((i+1, j))
    if (((i-1)>=0) and ((j+1)<column)) and arr[i-1][j+1]:
        li.append((i-1, j+1))
    if (j+1)<column and arr[i][j+1]:
        li.append((i, j+1))
    if (((i+1)<row) and ((j+1)<column)) and arr[i+1][j+1]:
        li.append((i+1, j+1))

    return li

def make_connection(arr, ar):

    col = len(arr[0])
    for i in range(len(arr)):

        for j in range(col):

            if arr[i][j]:
                pagli = i*col+j
                mylist = checkConnection(i,j)

                for r in mylist:
                    p, q = r
                    union(ar[pagli], ar[p*col+q])

row = int(input().strip())
column = int(input().strip())
length = row*column

arr = [[int(x) for x in input().split()] for _ in range(row)]
ar = length * [0]

for i in range(length):
    ar[i] = i

make_connection(arr, ar)
del arr

li = []
for i in range(length):
    li.append(findHead(ar[i]))
    
dic = {}
for i in range(length):
    try:
        dic[li[i]] += 1
    except:
        dic[li[i]] = 1

print(max(dic.values()))

