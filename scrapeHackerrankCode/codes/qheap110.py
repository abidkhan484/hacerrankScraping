# Wrong Answer
# Python 3

def add(p):
    mylist.append(p)
    length = len(mylist)-1
    # this part of the code just organise the element
    # according to the algorithm (bottom to top)
    while length:
        par = (length-1)//2
        if mylist[par] > mylist[length]:
            mylist[par] = mylist[length]
            length = par
            continue
        mylist[length] = p
        break

def move_to_top(pagli):
    # this loop moves the element to the Top
    i = pagli
    item = mylist[i]
    while pagli:
        par = (i-1)//2
        if mylist[par] > mylist[pagli]:
            mylist[pagli] = mylist[par]
            pagli = par
            continue
        break


def move_to_down(i):
    # this one Down the element
    length = len(mylist)
    item = mylist[i]
    childpos = (2*i)+1
    while childpos < length:
        rightpos = childpos + 1
        if rightpos < length and not mylist[childpos] < mylist[rightpos]:
            childpos = rightpos
        mylist[i] = mylist[childpos]
        i = childpos
        childpos = (2*i)+1
    mylist[i] = item


def delete(p):
    length = len(mylist)
    for i in range(length-1):
        if mylist[i]==p:
            mylist[i], mylist[-1] = mylist[-1], mylist[i]
            mylist.pop()
            break
    else:
        mylist.pop()
        return

    move_to_down(i)
    move_to_top(i)


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
'''input:
8
1 286789035
1 255653921
1 274310529
1 494521015
3
2 255653921
2 286789035
3

22
1 286789035
1 255653921
1 274310529
1 494521015
3
2 255653921
2 286789035
3
1 236295092
1 254828111
2 254828111
1 465995753
1 85886315
1 7959587
1 20842598
2 7959587
3
1 -51159108
3
2 -51159108
3
1 789534713'''

