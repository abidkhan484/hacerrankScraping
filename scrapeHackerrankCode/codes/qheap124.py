# Terminated due to timeout
# Python 3

def add(p):
    if p not in mylist:
        mylist.append(p)

def delete(p):
    for i in range(len(mylist)):
        if p==mylist[i]:
            del mylist[i]
            break

def printMin():
    print(min(mylist))
        
mylist = []
for _ in range(int(input().strip())):
    li = list(map(int, input().split()))
    if li[0]==1:
        add(li[1])
    elif li[0]==2:
        delete(li[1])
    else:
        printMin()

