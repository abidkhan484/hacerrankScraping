# Wrong Answer
# Python 3

def make_list(li, tmp, distance):

    mylist = []
    for i in tmp:
        # here i just add all the lists that are used for the next iteration
        if li[i-1] != 'read':
            mylist.extend(li[i-1])
            li[i-1] = 'read'

    mylist = list(set(mylist))
    mylist.sort()
    tmp = []

    # this for loop and the tmp list returns that items which are not read yet
    for i in mylist:
        if li[i-1]!='read':
            tmp.append(i)

    for i in tmp:
        # this problem has the same distance that is 6
        distance[i-1] += 6
    
    return li, tmp, distance


def bfs():
    node, edge = [int(i) for i in input().split()]

    li = [[] for _ in range(node)]
    # this is actually the input of the graph
    for _ in range(edge):
        p, i = [int(x) for x in input().split()]

        li[p-1].append(i)
        li[i-1].append(p)

    for i in range(node):
        li[i].sort()


    check = int(input().strip())
    distance = [0]*node; tmp = [check]; distance[check-1] = 1

    while tmp:
        li, tmp, distance = make_list(li, tmp, distance)

    for i in range(node):
        if not distance[i]:
            distance[i] = -1

    distance[check-1] = 0

    for i in distance:
        if i:
            print(i, end=' ')

def main():
    n = int(input().strip())
    for _ in range(n):
        bfs()
        print()

main()

