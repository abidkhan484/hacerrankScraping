# Terminated due to timeout
# Python 3

def add(p):
    mylist.append(p)
    length = len(mylist)-1
    while length:
        par = (length-1)//2
        if mylist[par] > mylist[length]:
            mylist[par], mylist[length] = mylist[length], mylist[par]
            length = par
        else:
            break

def delete(p):
    length = len(mylist)
    for i in range(length-1):
        if mylist[i]==p:
            mylist[i], mylist[-1] = mylist[-1], mylist[i]
            mylist.pop()
            break
    else:
        mylist.pop()

    pagli = i
    while pagli:
        par = (i-1)//2
        if mylist[par] > mylist[pagli]:
            mylist[pagli], mylist[par] = mylist[par], mylist[pagli]
            pagli = par
        else:
            break

    while i < length:
        child1 = (2*i)+1
        child2 = (2*i)+2

        if child1 < length-1:
            if mylist[child1] < mylist[i]:
                mylist[child1], mylist[i] = mylist[i], mylist[child1]
                i = child1
        elif child2 < length:
            if mylist[child2] < mylist[i]:
                mylist[child2], mylist[i] = mylist[i], mylist[child2]
                i = child2
        else:
            break

def printMin():
    if mylist:
        print(mylist[0])

mylist = []
'''add(9);add(5);add(2);add(11);add(22);add(4); add(3); add(6)
print(mylist)
delete(6)
print(mylist)
'''
for _ in range(int(input().strip())):
    li = list(map(int, input().split()))
    if li[0]==1:
        add(li[1])
    elif li[0]==2:
        delete(li[1])
    else:
        printMin()

