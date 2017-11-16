# Terminated due to timeout
# Python 3

def add(p):
    mylist.append(p)
    length = len(mylist)-1
    # this part of the code just organise the element
    # according to the algorithm (bottom to top)
    while length:
        par = (length-1)//2
        if mylist[par] > mylist[length]:
            mylist[par], mylist[length] = mylist[length], mylist[par]
            length = par
        else:
            break

def move_to_top(pagli):
    # this loop moves the element to the Top
    i = pagli
    while pagli:
        par = (i-1)//2
        if mylist[par] > mylist[pagli]:
            mylist[pagli], mylist[par] = mylist[par], mylist[pagli]
            pagli = par
        else:
            break


def move_to_down(i, queue=[]):
    # this one Down the element
    length = len(mylist)
    while i < length:
        child1 = (2*i)+1
        child2 = (2*i)+2
        if child1 < length:
            if mylist[child1] < mylist[i]:
                mylist[child1], mylist[i] = mylist[i], mylist[child1]
                # this list'll check the li if it had any error after swap
                ch1 = (i*2)+1; ch2 = (i*2)+2
                if (mylist[i] < mylist[ch1]) or (mylist[i] < mylist[ch2]):
                    queue.append(i)
                i = child1
                continue
        if child2 < length:
            if mylist[child2] < mylist[i]:
                mylist[child2], mylist[i] = mylist[i], mylist[child2]
                i = child2
                continue

        return queue

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

    queue = move_to_down(i)
    move_to_top(i)

    for i in queue:
        move_to_down(i)


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

