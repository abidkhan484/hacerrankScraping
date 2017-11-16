# Accepted
# Python 3

# this function return what are the towns, they are connected
def find_connections(mylist, i):
    # towns var counts how many towns are connected
    tmp = []; towns = 0
    tmp.extend(mylist[i-1])

    while tmp:
        li = []
        for j in tmp:
            if mylist[j-1] != 'read':
                towns += 1
                li.extend(mylist[j-1])
                mylist[j-1] = 'read'
        tmp = list(set(li))

    if not towns:
        return towns
    return towns-1
    

def check_cost():
    node, edge, libCost, roadCost = [int(x) for x in input().split()]
    mylist = [[] for i in range(node)]

    for _ in range(edge):
        n, m = [int(x) for x in input().split()]

        mylist[n-1].append(m)
        mylist[m-1].append(n)


    if libCost <= roadCost:
        print(node*libCost)
        return

    connected_count = 0; towns=0
    for i in range(node):
        if mylist[i] != 'read':
            towns += find_connections(mylist, i+1)
            # it counts how many time i need to call the function 'find_connections'
            connected_count += 1
    
    print((towns*roadCost)+(connected_count*libCost))    

def main():
    n = int(input().strip())
    for _ in range(n):
        check_cost()

main()

