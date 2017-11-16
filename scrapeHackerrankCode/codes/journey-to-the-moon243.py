# Terminated due to timeout
# Python 3

def find_connections(mylist, i):
    # towns var counts how many towns are connected
    tmp = []; same_citizen = 0
    tmp.extend(mylist[i-1])

    while tmp:
        li = []
        for j in tmp:
            if mylist[j-1] != 'read':
                same_citizen += 1
                li.extend(mylist[j-1])
                mylist[j-1] = 'read'
        tmp = list(set(li))
    if not same_citizen:
        return same_citizen+1
    return same_citizen
    

def journey_pair():
    node, edge = [int(x) for x in input().split()]
    mylist = [[] for i in range(node)]

    for _ in range(edge):
        n, m = [int(x) for x in input().split()]

        mylist[n-1].append(m)
        mylist[m-1].append(n)

    pair = 0
    li = []
    for i in range(node):
        if mylist[i] != 'read':
            same_citizen = find_connections(mylist, i+1)
            li.append(same_citizen)

    del mylist

    length = len(li)
    for i in range(length-1):
        j = i+1
        while j<length:
            pair += (li[i] * li[j])
            j += 1

    print(pair)

journey_pair()

