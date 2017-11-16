# Wrong Answer
# Python 3

def find_connections(mylist, i):
    # same_citizen var counts how many towns are connected
    tmp = []; same_citizen = 0; city_sum = 0
    tmp.extend(mylist[i-1])

    while tmp:
        li = []
        for j in tmp:
            if mylist[j-1] != 'read':
                same_citizen += 1
                li.extend(mylist[j-1])
                mylist[j-1] = 'read'
        tmp = list(set(li))
        city_sum += len(tmp)
  
    return same_citizen, city_sum
    

def journey_pair():
    node, edge = [int(x) for x in input().split()]
    mylist = [[] for i in range(node)]

    for _ in range(edge):
        n, m = [int(x) for x in input().split()]

        mylist[n-1].append(m)
        mylist[m-1].append(n)

    pair = 0; city_sum = 0
    li = []
    for i in range(node):
        if mylist[i] != 'read':
            same_citizen, summation = find_connections(mylist, i+1)
            if same_citizen:
                li.append(same_citizen)
            city_sum += summation

    del mylist

    length = len(li)
    for i in range(length-1):
        j = i+1
        while j<length:
            pair += (li[i] * li[j])
            j += 1
    singles = node-city_sum
    singles_pair = (singles*(singles-1))//2

    pair = pair + singles_pair + (singles*city_sum)
    
    print(pair)

journey_pair()

